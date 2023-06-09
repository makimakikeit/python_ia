from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('article/list/', views.ArticleListView.as_view(), name='article_list'),
    path('article/detail/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('tag/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('article/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('tag/list/', views.TagListView.as_view(), name='tag_list'),
]