from rest_framework import generics
from rest_framework.generics import get_object_or_404

from permissions.permissions import IsAuthorOrReadOnly
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer, PostImageSerializer


class PostList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.prefetch_related('category').select_related('author').all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(queryset, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(queryset, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj


class PostImagesList(generics.ListAPIView):
    queryset = Post.objects.exclude(image__isnull=True).exclude(image='').order_by('-created_at')
    serializer_class = PostImageSerializer
