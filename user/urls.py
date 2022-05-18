
from codecs import namereplace_errors
from django.urls import path
from . import views

urlpatterns = [
path('register',views.register,name="registerUrl"),
path('login',views.login,name="loginUrl"),
path('logout',views.Logout,name="logoutUrl"),
]
