from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('graphs/', views.graphs, name='graphs'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('signup/', views.signup, name='signup'),
    path('analysis/', views.analysis, name='analysis'),
]
