import rules
from rules.predicates import is_superuser

from .predicates import is_initiator

rules.add_perm('euth_organisations.modify_organisation',
               is_superuser | is_initiator)
