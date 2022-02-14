from . import models
from . import serializers
from rest_framework import viewsets, permissions,response,status

class CompanyReportViewSet(viewsets.ModelViewSet):
    """ViewSet for the Company Report class"""

    queryset = models.CompanyReport.objects.all()
    serializer_class = serializers.CompanyReportSerializers
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = dict(request.data) 

        data["user"] = request.user.id
        print (data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)