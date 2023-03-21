from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='posts/images/categories')
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=120, blank=True, null=True, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to='posts/images/posts')
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    def published_date(self):
        return self.created_at.strftime('%B %d, %Y')

    @property
    def summary(self):
        return self.body[:300] + "..."

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def __str__(self):
        return self.title
