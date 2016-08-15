from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response

from . import emails
from .models import Report
from .serializers import ReportSerializer


class ReportViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request):
        """
        Sets the user of the request as user of the report
        """
        serializer = ReportSerializer(data=request.data)

        if serializer.is_valid():
            report = serializer.save(user=self.request.user)
            emails.send_email_to_moderators(request, report)
            emails.send_email_to_creator(request, report)

            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
