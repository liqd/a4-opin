import rules
from rules.predicates import is_superuser

from adhocracy4.modules.predicates import (is_context_initiator,
                                           is_context_member,
                                           is_context_moderator, is_owner,
                                           is_public_context)
from adhocracy4.phases.predicates import (phase_allows_add,
                                          phase_allows_change,
                                          phase_allows_comment,
                                          phase_allows_rate)

from .models import Topic

rules.add_perm('euth_communitydebate.comment_topic',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_comment))


rules.add_perm('euth_communitydebate.modify_topic',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & is_owner & phase_allows_change))


rules.add_perm('euth_communitydebate.propose_topic',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_add(Topic)))


rules.add_perm('euth_communitydebate.rate_topic',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_rate))


rules.add_perm('euth_communitydebate.view_topic',
               is_superuser | is_context_moderator | is_context_initiator |
               is_context_member | is_public_context)
