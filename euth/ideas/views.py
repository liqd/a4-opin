from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db.models import FieldDoesNotExist
from django.db.models.expressions import RawSQL
from django.utils.translation import ugettext as _
from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from euth.modules.models import Module
from euth.projects import mixins

from . import forms, models


class IdeaListView(mixins.ProjectMixin, generic.ListView):
    model = models.Idea

    def get_queryset(self):
        sort = self.request.GET.get('sort')
        qs = models.Idea.objects.filter(module=self.module)
        if sort:
            if sort == 'ratings':
                contenttype = ContentType.objects.get(
                    app_label="euth_ideas", model="idea")
                query_string = RawSQL('select COUNT(*) '
                                      'from "euth_ratings_rating"'
                                      'where '
                                      '"content_type_id" = %s '
                                      'and "object_pk" '
                                      '= "euth_modules_item"."id" '
                                      'and "value" = 1',
                                      (contenttype.id,))
                qs = qs.annotate(ratings_count=query_string)

                return qs.order_by('-ratings_count')
            else:
                try:
                    models.Idea._meta.get_field_by_name(sort)
                    return qs.order_by(sort)
                except FieldDoesNotExist:
                    return qs.order_by('name')

        else:
            return qs.order_by('name')


class IdeaDetailView(PermissionRequiredMixin, generic.DetailView):
    model = models.Idea
    permission_required = 'euth_ideas.view_idea'


class IdeaUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = models.Idea
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
    model = models.Idea
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
    model = models.Idea
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
