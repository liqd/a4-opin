import xlsxwriter
from django.http import HttpResponse
from django.utils import timezone
from django.utils.html import strip_tags
from django.views import generic


class CommentsExportMixin:
    COMMENT_FMT = '{date} - {username}\n{text}'
    REPLY_FMT = '@reply: {date} - {username}\n{text}'

    def get_comments_data(self, comments):
        return '\n----\n'.join(self._flat_comments(comments))

    def _flat_comments(self, comments):
        for comment in comments.all():
            yield self.COMMENT_FMT.format(
                date=comment.created.isoformat(),
                username=comment.creator.username,
                text=strip_tags(comment.comment).strip()
            )
            for reply in comment.child_comments.all():
                yield self.REPLY_FMT.format(
                    date=reply.created.isoformat(),
                    username=reply.creator.username,
                    text=strip_tags(reply.comment).strip()
                )


class XlsExporterMixin(generic.ListView, CommentsExportMixin):
    export_comments = False
    export_ratings = False

    def get_fields(self):
        return []

    def _get_final_fields(self):
        final_fields = self.get_fields()
        if self.export_comments:
            final_fields.append('comments')
        if self.export_ratings:
            final_fields.append('positive_rating_count')
            final_fields.append('negative_rating_count')
        return final_fields

    def get_filename(self):
        filename = \
            'export_%s.xlsx' % (timezone.now().strftime('%Y%m%dT%H%M%S'))
        return filename

    def _write_header(self, worksheet):
        final_fields = self._get_final_fields()
        for index, field in enumerate(final_fields):
            worksheet.write(0, index, field)

    def _write_table(self, worksheet):
        row = 1
        for item in self.get_queryset():
            for col, field in enumerate(self._get_final_fields()):
                if field == "comments":
                    worksheet.write(row, col,
                                    self.get_comments_data(item.comments))
                else:
                    worksheet.write(row, col, str(getattr(item, field)))
            row += 1

    def _write_workbook(self, response):
        workbook = xlsxwriter.Workbook(
            response, {'in_memory': True, 'remove_timezone': True})
        worksheet = workbook.add_worksheet()

        self._write_header(worksheet)
        self._write_table(worksheet)

        workbook.close()

    def get(self, request, *args, **kwargs):
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument'
                         '.spreadsheetml.sheet')
        response['Content-Disposition'] = \
            'attachment; filename="%s"' % self.get_filename()

        self._write_workbook(response)
        return response
