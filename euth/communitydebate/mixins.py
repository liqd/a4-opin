from django.forms import modelformset_factory

from .forms import TopicFileUploadForm
from .models import TopicFileUpload


class TopicFormMixin:

    def update_upload_formset(self, queryset):
        return modelformset_factory(
            TopicFileUpload,
            TopicFileUploadForm,
            extra=1, max_num=3, can_delete=True)(queryset=queryset)

    def filled_upload_formset(self, request):
        return modelformset_factory(
            TopicFileUpload,
            TopicFileUploadForm,
            extra=1, max_num=3, can_delete=True)(request.POST, request.FILES)

    def empty_upload_formset(self):
        queryset = TopicFileUpload.objects.none()
        return modelformset_factory(
            TopicFileUpload,
            TopicFileUploadForm,
            extra=1, max_num=3, can_delete=True)(queryset=queryset)
