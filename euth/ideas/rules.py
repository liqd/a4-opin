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

from .models import Idea

rules.add_perm('euth_ideas.rate_idea',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_rate))


rules.add_perm('euth_ideas.comment_idea',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_comment))


rules.add_perm('euth_ideas.modify_idea',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & is_owner & phase_allows_change))


rules.add_perm('euth_ideas.propose_idea',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_add(Idea)))


rules.add_perm('euth_ideas.view_idea',
               is_superuser | is_context_moderator | is_context_initiator |
               is_context_member | is_public_context)

rules.add_perm('euth_ideas.export_ideas',
               is_superuser | is_context_moderator | is_context_initiator)
