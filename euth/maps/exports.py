from django.utils.translation import ugettext_lazy as _

from adhocracy4.exports import mixins as a4_export_mixins
from adhocracy4.exports import views as a4_export_views
from euth.exports import register_export
from euth.exports.mixins import ItemExportWithLocationMixin

from . import models


@register_export(_('MapIdeas with comments'))
class MapIdeaExportView(a4_export_mixins.ItemExportWithLinkMixin,
                        a4_export_mixins.ExportModelFieldsMixin,
                        ItemExportWithLocationMixin,
                        a4_export_mixins.ItemExportWithRatesMixin,
                        a4_export_mixins.ItemExportWithCategoriesMixin,
                        a4_export_mixins.ItemExportWithCommentCountMixin,
                        a4_export_mixins.ItemExportWithCommentsMixin,
                        a4_export_views.BaseItemExportView):

    model = models.MapIdea
    fields = ['name', 'description']
    html_fields = ['description']

    def get_queryset(self):
        return super().get_queryset() \
            .filter(module=self.module)\
            .annotate_comment_count()\
            .annotate_positive_rating_count()\
            .annotate_negative_rating_count()
