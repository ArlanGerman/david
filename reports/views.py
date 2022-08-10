from rest_framework import generics
from oauth2_provider.contrib.rest_framework import IsAuthenticatedOrTokenHasScope
from reports.models import DailyReportsModel
from reports.serializers import ReportsModelSerializer
from rest_framework import status
from rest_framework.response import Response

class ReportsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReportsModelSerializer
    permissions_classes = [IsAuthenticatedOrTokenHasScope]
    required_scopes = ["read", "write"]

    def get_queryset(self):
        return DailyReportsModel.objects.filter(author=self.request.user.pk)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={**request.data, 'author': request.user.pk})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ReportsRetrieveUpdateDestroyRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyReportsModel.objects.all()
    serializer_class = ReportsModelSerializer
    permissions_classes = [IsAuthenticatedOrTokenHasScope]
    required_scopes = ["read", "write"]