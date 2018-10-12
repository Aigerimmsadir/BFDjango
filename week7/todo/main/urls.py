from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('/home', views.index, name='index'),
    path('1/completed/', views.completed_tasks,name='completed'),
    path('1/incompleted/', views.incompleted_tasks,name="incompleted"),
   	
    path('1/creation_order/', views.creation_order,name='creation'),
    path('1/due_order/', views.due_order,name='due_order'),

    path('1/delete_task/<int:task_id>', views.delete_task,name="delete_task"),
    path('1/delete_list/', views.delete_list,name="delete_list"),
    path('1/task_done/<int:task_id>', views.task_done,name="task_done"),
    path('1/add_task/', views.add_task,name="add_task"),
    path('1/update_task/<int:task_id>',views.update_task, name='update_task')
]