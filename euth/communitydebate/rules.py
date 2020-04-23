import rules
from rules.predicates import is_superuser

from adhocracy4.modules.predicates import (is_context_initiator,
                                           is_context_member,
                                           is_context_moderator, is_owner)
from adhocracy4.phases.predicates import phase_allows_change

rules.add_perm('euth_communitydebate.modify_topic',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & is_owner & phase_allows_change))
