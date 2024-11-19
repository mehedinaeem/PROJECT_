
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('home/',views.home,name='home'),
   path("accounts/", include("django.contrib.auth.urls")),
   path("signup/", views.authView,name="authView"),
]
