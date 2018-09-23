from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1/completed/', views.completed_tasks),
    path('1/incompleted/', views.incompleted_tasks),
    path('1/due/', views.tasks_due),
    path('1/creation_order/', views.creation_order),
    path('1/due_order/', views.due_order)
]