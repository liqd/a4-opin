import rules
from rules.predicates import is_superuser

from adhocracy4.modules.predicates import (is_context_initiator,
                                           is_context_member,
                                           is_context_moderator)
from adhocracy4.phases.predicates import phase_allows_create

from .models import MapIdea

rules.add_perm('euth_maps.propose_idea',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_create(MapIdea)))
