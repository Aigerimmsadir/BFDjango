from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('list/', views.task_list_jsn, name = 'list'),
    path('list/<int:pk>', views.task_read, name = 'list_read'),
    path('list/completed', views.task_completed, name = 'list_completed'),
    path('task_list/', views.TaskList.as_view(), name='task_list'),
    path('task_detail/<int:pk>', views.TaskDetail.as_view(), name='task_detail'),
    path('register/',views.UserCreate.as_view()),
    path('login/', views.login ),
    path('gen_list/',views.GenericTaskList.as_view()),
    path('get_detail/',views.GenericTaskDetail.as_view()),
    path('user/',views.current_user),
]

