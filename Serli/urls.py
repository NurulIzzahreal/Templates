from django.urls import path
from . import views

urlpatterns = [
    path('Serli/', views.Serli, name='Serli'),
]