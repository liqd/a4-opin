from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.modules.models import Module
from adhocracy4.projects import mixins
from euth.contrib.exports import XlsExporterMixin
from euth.projects import mixins as prj_mixins

from . import models as idea_models
from . import forms


class SortMixin():
    sort_default = None
    sorts = []
    sort = None

    def get_sort(self):
        sort = self.request.GET.get('sort') or self.sort_default
        sorts = dict(self.sorts).keys()
        if sort not in sorts:
            sort = self.sort_default
        return sort

    def get_queryset(self):
        qs = super().get_queryset()
        self.sort = self.get_sort()

        if not self.sort:
            return qs

        return qs.order_by(self.sort)

    def get_current_sortname(self):
        if self.sort:
            return dict(self.sorts)[self.sort]


class IdeaListView(
    mixins.ProjectMixin,
    SortMixin,
    generic.ListView,
    prj_mixins.ProjectPhaseMixin
):
    model = idea_models.Idea
    paginate_by = 15
    sort_default = '-created'
    sorts = [
        ('-created', _('Most recent')),
        ('-positive_rating_count', _('Popularity')),
        ('-comment_count', _('Comments'))
    ]

    def get_queryset(self):
        return super().get_queryset().filter(module=self.module) \
            .annotate_positive_rating_count() \
            .annotate_negative_rating_count() \
            .annotate_comment_count()


class IdeaDetailView(PermissionRequiredMixin, generic.DetailView):
    model = idea_models.Idea
    queryset = idea_models.Idea.objects.annotate_positive_rating_count() \
        .annotate_negative_rating_count()
    permission_required = 'euth_ideas.view_idea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_is_moderator'] = self.object.creator in self.object. \
            project.moderators.all()
        return context


class IdeaUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = idea_models.Idea
    form_class = forms.IdeaForm
    permission_required = 'euth_ideas.modify_idea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        context['mode'] = 'update'
        return context


class IdeaCreateView(PermissionRequiredMixin, generic.CreateView):
    model = idea_models.Idea
    form_class = forms.IdeaForm
    permission_required = 'euth_ideas.propose_idea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def dispatch(self, *args, **kwargs):
        mod_slug = self.kwargs[self.slug_url_kwarg]
        self.module = Module.objects.get(slug=mod_slug)
        self.project = self.module.project
        return super().dispatch(*args, **kwargs)

    def get_permission_object(self, *args, **kwargs):
        return self.module

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.module.slug
        context['project'] = self.project
        context['mode'] = 'create'
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.module = self.module
        return super().form_valid(form)


class IdeaDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = idea_models.Idea
    success_message = _("Your Idea has been deleted")
    permission_required = 'euth_ideas.modify_idea'

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(IdeaDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project-detail',
                       kwargs={'slug': self.object.project.slug})


class IdeaDownloadView(PermissionRequiredMixin,
                       XlsExporterMixin,
                       prj_mixins.ModuleMixin):

    permission_required = "euth_ideas.export_ideas"
    model = idea_models.Idea
    export_comments = True
    export_ratings = True

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def get_queryset(self):
        return super().get_queryset().filter(module=self.module) \
            .annotate_positive_rating_count() \
            .annotate_negative_rating_count() \
            .annotate_comment_count()

    def get_filename(self):
        project = self.module.project
        filename = '%s_%s.xlsx' % (project.slug,
                                   timezone.now().strftime('%Y%m%dT%H%M%S'))
        return filename

    def get_fields(self):
        idea_fields = idea_models.Idea._meta.concrete_fields
        excludes = ['creator_id', 'item_ptr_id', 'module_id',
                    'item_ptr', 'slug', 'module']
        final_fields = [field.name for field in idea_fields if
                        field.name not in excludes]
        return final_fields
