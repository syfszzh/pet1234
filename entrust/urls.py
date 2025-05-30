from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.entrust_form, name='entrust_form'),
]