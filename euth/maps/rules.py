import rules
from rules.predicates import is_superuser

from adhocracy4.modules.predicates import is_context_initiator
from adhocracy4.modules.predicates import is_context_member
from adhocracy4.modules.predicates import is_context_moderator
from adhocracy4.modules.predicates import is_owner
from adhocracy4.modules.predicates import is_public_context
from adhocracy4.phases.predicates import phase_allows_add
from adhocracy4.phases.predicates import phase_allows_change
from adhocracy4.phases.predicates import phase_allows_comment
from adhocracy4.phases.predicates import phase_allows_rate

from .models import MapIdea

rules.add_perm('euth_maps.rate_mapidea',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_rate))


rules.add_perm('euth_maps.comment_mapidea',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_comment))


rules.add_perm('euth_maps.modify_mapidea',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & is_owner & phase_allows_change))


rules.add_perm('euth_maps.propose_mapidea',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_add(MapIdea)))


rules.add_perm('euth_maps.view_mapidea',
               is_superuser | is_context_moderator | is_context_initiator |
               is_context_member | is_public_context)
