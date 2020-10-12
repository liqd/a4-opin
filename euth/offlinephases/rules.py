import rules
from rules.predicates import is_superuser

from adhocracy4.modules.predicates import is_context_initiator
from adhocracy4.modules.predicates import is_context_member
from adhocracy4.modules.predicates import is_context_moderator
from adhocracy4.modules.predicates import is_public_context

from .predicates import is_offlinephase_moderator

rules.add_perm(
    'euth_offlinephases.modify_offlinephase',
    is_offlinephase_moderator | is_superuser)

rules.add_perm('euth_offlinephases.view_offlineevent',
               is_superuser | is_context_moderator | is_context_initiator |
               is_context_member | is_public_context)
