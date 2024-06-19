from django.urls import path
from .views import index, SignUp
  # Import the signup view

urlpatterns = [
    path('', index, name='index'),
   path('SignUp.html', SignUp, name='SignUp'),
path('index.html', index, name='index')
]
