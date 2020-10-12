import rules
from rules.predicates import is_superuser

from adhocracy4.modules.predicates import is_context_initiator
from adhocracy4.modules.predicates import is_context_member
from adhocracy4.modules.predicates import is_context_moderator
from adhocracy4.modules.predicates import is_public_context
from adhocracy4.phases.predicates import phase_allows_comment

rules.add_perm('euth_documents.comment_paragraph',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_comment))

rules.add_perm('euth_documents.comment_document',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_comment))

rules.add_perm('euth_documents.add_document',
               is_superuser | is_context_moderator | is_context_initiator)

rules.add_perm('euth_documents.change_document',
               is_superuser | is_context_moderator | is_context_initiator)

rules.add_perm('euth_documents.create_document',
               is_superuser | is_context_moderator | is_context_initiator)

rules.add_perm('euth_documents.view_paragraph',
               is_superuser | is_context_moderator | is_context_initiator |
               is_context_member | is_public_context)
