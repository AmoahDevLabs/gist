from rest_framework import serializers
from .models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.get_full_name', read_only=True)
    category = serializers.CharField(source='category.title')
    summary = serializers.CharField(read_only=True)
    published_date = serializers.DateTimeField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'category', 'slug', 'image', 'body', 'summary', 'author', 'published_date',)


class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'slug', 'posts')


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['slug', 'image']
