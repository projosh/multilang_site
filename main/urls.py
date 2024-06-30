from django.urls import path
from . import views

urlpatterns = [
     path('', views.article_list, name='article_list'),  # List of articles
    path('delete/<int:article_id>/', views.delete_article, name='delete_article'),  # Delete article
    path('add/', views.add_article, name='add_article'),  # Add article
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),  # Article detail
]
   


