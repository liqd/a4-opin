import rules
from rules.predicates import is_superuser


from .predicates import is_offlinephase_moderator

rules.add_perm(
    'euth_offlinephases.modify_offlinephase',
    is_offlinephase_moderator | is_superuser)
