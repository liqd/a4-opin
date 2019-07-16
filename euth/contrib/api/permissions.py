from rest_framework import permissions


class IsInitiatorOrSuperUser(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.

    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        is_initiator = obj.organisation.initiators.filter(pk=request.user.pk)\
            .exists()
        return request.user.is_superuser or is_initiator
