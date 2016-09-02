import rules
from rules.predicates import is_superuser

from .predicates import is_initiator, is_live, is_member, is_public

rules.add_perm('projects.view_project',
               is_superuser | is_initiator |
               ((is_public | is_member) & is_live))
