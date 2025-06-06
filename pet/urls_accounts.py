from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, register

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]