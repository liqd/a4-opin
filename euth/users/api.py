from rest_framework import filters, serializers, viewsets

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
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
