from django.forms import modelformset_factory

from .forms import FileUploadForm
from .models import OfflineEventFileUpload


class OfflineEventFormMixin:

    def empty_upload_formset(self):
        queryset = OfflineEventFileUpload.objects.none()
        return modelformset_factory(
            OfflineEventFileUpload,
            FileUploadForm,
            extra=1, max_num=5, can_delete=True)(queryset=queryset)

    def update_upload_formset(self, queryset):
        return modelformset_factory(
            OfflineEventFileUpload,
            FileUploadForm,
            extra=1, max_num=5, can_delete=True)(queryset=queryset)

    def filled_upload_formset(self, request):
        return modelformset_factory(
            OfflineEventFileUpload,
            FileUploadForm,
            extra=1, max_num=5, can_delete=True)(request.POST, request.FILES)
