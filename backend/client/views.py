from rest_framework import generics, views, permissions
from backend.models import Client
from .serializers import ClientSerializer


class ClientList(generics.ListAPIView):
    serializer_class = ClientSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = Client.objects.filter(created_by = user)
        if user.is_superuser:
            queryset = Client.objects.all()
        return queryset


class ClientCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ClientRetrieve(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    


class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
