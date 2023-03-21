from django.urls import path
from ..views import PostList, PostDetail, PostImagesList

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('images/', PostImagesList.as_view()),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
