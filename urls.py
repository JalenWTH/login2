from django.urls import path
from . import views

urlpatterns = [
	path('home', views.Home, name='Home'),
	path('login', views.Login, name='Login'),
	path('signup', views.Signup, name='Signup'),
]