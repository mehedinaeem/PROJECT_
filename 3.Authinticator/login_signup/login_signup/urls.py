
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',include('base.urls')),
    path('',views.pro_home,name='pro'),
]
