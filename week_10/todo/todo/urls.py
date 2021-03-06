from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('auth_.urls')),
    path('cbv/', include('cbv.urls')),
    path('api2/', include('api2.urls')),
]