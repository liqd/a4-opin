import rules
from rules.predicates import is_superuser

from euth.modules.predicates import (is_context_member, is_context_moderator,
                                     is_owner)
from euth.phases.predicates import phase_allows_create, phase_allows_modify

from .models import Idea

rules.add_perm('ideas.modify_idea',
               is_superuser | is_context_moderator |
               (is_context_member & is_owner & phase_allows_modify))


rules.add_perm('euth_ideas.propose_idea',
               is_superuser | is_context_moderator |
               (is_context_member & phase_allows_create(Idea)))
