from rest_framework import generics, views, permissions
from backend.models import Article
from .serializers import ArticleSerializer


class ArticleList(generics.ListAPIView):
    serializer_class = ArticleSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = Article.objects.filter(created_by = user)
        if user.is_superuser:
            queryset = Article.objects.all().order_by("-id")
        return queryset


class ArticleCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ArticleRetrieve(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
