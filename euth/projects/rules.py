import rules
from rules.predicates import is_superuser

rules.add_perm("euth_projects.add_project", is_superuser)

rules.add_perm("euth_projects.change_project", is_superuser)
