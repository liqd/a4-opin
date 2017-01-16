import rules

from .predicates import is_offlinephase_moderator

rules.add_perm(
    'euth_offlinephases.modify_offlinephase', is_offlinephase_moderator)
