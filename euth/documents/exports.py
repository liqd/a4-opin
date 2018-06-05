from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from adhocracy4.comments.models import Comment
from adhocracy4.exports import mixins as export_mixins
from adhocracy4.exports import views as export_views
from euth.exports import mixins as euth_export_mixins
from euth.exports import register_export


@register_export(_('Documents with comments'))
class DocumentExportView(
        export_mixins.ExportModelFieldsMixin,
        euth_export_mixins.UserGeneratedContentExportMixin,
        export_mixins.ItemExportWithLinkMixin,
        export_mixins.ItemExportWithRatesMixin,
        euth_export_mixins.ItemExportWithRepliesToMixin,
        export_views.BaseItemExportView
):

    model = Comment

    fields = ['id', 'comment', 'created']

    def get_queryset(self):
        try:
            return self.module.item_set.first().document.clustered_comments
        except AttributeError:
            return Comment.objects.none()

    def get_base_filename(self):
        return '%s_%s' % (self.project.slug,
                          timezone.now().strftime('%Y%m%dT%H%M%S'))
