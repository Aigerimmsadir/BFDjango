from django.urls import path
from api2 import views

urlpatterns = [
    path('tasks/', views.tasks_list),
    path('tasks/<int:pk>/', views.tasks_detail)
]
