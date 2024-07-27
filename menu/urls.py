from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('about/team/', views.team, name='team'),
    path('services/', views.services, name='services'),
    path('services/development/', views.development, name='development'),
    path('services/design/', views.design, name='design'),
]
