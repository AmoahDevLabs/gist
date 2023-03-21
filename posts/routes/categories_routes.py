from django.urls import path
from ..views import CategoryList, CategoryDetail

urlpatterns = [
    path('', CategoryList.as_view(), name='category_list'),
    path('<slug:slug>/', CategoryDetail.as_view(), name='category_detail'),
]
