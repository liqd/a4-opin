import rules
from rules.predicates import is_superuser

from adhocracy4.modules.predicates import (is_context_initiator,
                                           is_context_member,
                                           is_context_moderator,
                                           is_owner,
                                           is_public_context)
from adhocracy4.phases.predicates import (phase_allows_comment,
                                          phase_allows_create,
                                          phase_allows_modify,
                                          phase_allows_rate)
from .models import MapIdea


rules.add_perm('euth_maps.rate_mapidea',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_rate))


rules.add_perm('euth_maps.comment_mapidea',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_comment))


rules.add_perm('euth_maps.modify_mapidea',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & is_owner & phase_allows_modify))


rules.add_perm('euth_maps.propose_mapidea',
               is_superuser | is_context_moderator | is_context_initiator |
               (is_context_member & phase_allows_create(MapIdea)))


rules.add_perm('euth_maps.view_mapidea',
               is_superuser | is_context_moderator | is_context_initiator |
               is_context_member | is_public_context)
