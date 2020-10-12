from django.db.models.functions import Lower
from rest_framework import filters
from rest_framework import permissions
from rest_framework import serializers
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = User.objects.all().order_by(Lower('username'))
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^username',)

    def list(self, request, *args, **kwargs):
        is_no_search = not (hasattr(request, 'query_params') and
                            'search' in request.query_params and
                            len(request.query_params['search']) > 0)
        if is_no_search:
            raise serializers.ValidationError(
                detail='Only usable with search.')
        return super().list(request, *args, **kwargs)
