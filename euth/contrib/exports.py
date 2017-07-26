from django.utils.html import strip_tags


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
