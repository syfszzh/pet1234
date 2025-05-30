from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('pet/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('apply/<int:pet_id>/', views.adoption_apply, name='adoption_apply'),
    path('', views.about, name='about'),
    path('adoption/', views.adoption, name='adoption'),
    path('corporate-adoption/', views.corporate_adoption, name='corporate_adoption')
]