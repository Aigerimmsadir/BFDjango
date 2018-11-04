from django.urls import path
from . import views

urlpatterns = [
    path('posts/',views.posts_list),
    path('posts/<int:pk>/', views.posts_detail)
]   