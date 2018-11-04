from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('read_post/<int:post_id>',views.read_post,name='read_post'),
    path('add_post/',views.add_post,name="add_post"),
    path('update_post/<int:post_id>',views.update_post,name="update_post"),
    path('delete_post/<int:post_id>',views.delete_post,name="delete_post"),
    path('add_comment/<int:post_id>',views.add_comment,name="add_comment")
]   