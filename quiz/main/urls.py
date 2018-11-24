from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('advert_list/',views.AdvertList.as_view()),
    path('advert_detail/<int:pk>',views.AdvertDetail.as_view()),
    path('advert_list_fbv/',views.advert_list),
    path('advert_detail_fbv/<int:pk>', views.advert_detail),
    path('login/', views.login ),
    ]


