from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),  # List of articles
    path('delete/<int:article_id>/', views.delete_article, name='delete_article'),  # Delete article
    path('create/new/', views.create_article, name='create_article'),
    path('article/<int:article_id>/edit/', views.article_update, name='article_update'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),  # Article detail
]
   


