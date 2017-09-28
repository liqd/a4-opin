from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from adhocracy4.categories import filters as cat_filters
from adhocracy4.filters import views as filter_views
from adhocracy4.filters import filters
from adhocracy4.modules.models import Module
from adhocracy4.projects import mixins
from euth.contrib import exports
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


class IdeaFilterSet(filters.DefaultsFilterSet):
    defaults = {}
    category = cat_filters.CategoryFilter()

    class Meta:
        model = idea_models.Idea
        fields = ['category']


class IdeaListView(
    mixins.ProjectMixin,
    SortMixin,
    prj_mixins.ProjectPhaseMixin,
    filter_views.FilteredListView
):
    model = idea_models.Idea
    paginate_by = 15
    sort_default = '-created'
    filter_set = IdeaFilterSet
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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['module'] = kwargs.get('instance').module
        return kwargs


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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['module'] = self.module
        return kwargs


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


class IdeaDownloadView(prj_mixins.ModuleMixin,
                       PermissionRequiredMixin,
                       exports.ItemExportView,
                       exports.ItemExportWithRatesMixin,
                       exports.ItemExportWithCommentCountMixin,
                       exports.ItemExportWithCommentsMixin,
                       exports.ItemExportWithCategoriesMixin
                       ):

    model = idea_models.Idea
    permission_required = "euth_ideas.export_ideas"
    fields = ['name', 'description', 'creator', 'created']

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()

    def get_queryset(self):
        return super().get_queryset() \
            .filter(module=self.module)\
            .annotate_comment_count()\
            .annotate_positive_rating_count()\
            .annotate_negative_rating_count()

    def get_permission_object(self, *args, **kwargs):
        return self.module
