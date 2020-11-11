from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
        
        path('',views.portada ,name=''),
        path('principal',views.principal ,name='principal'),
        path('registro',views.registro ,name='registro'),
        path('login',views.login ,name='login'),
        path('nosotros',views.nosotros ,name='nosotros'),
        path('Admin', views.Admin, name='Admin'),
        path('carro',views.carro,name='carro'),
        path('Maui',views.Maui,name='Maui'),
        path('collokey',views.collokey,name='collokey'),
]

#127.0.0.1:8000/

#127.0.0.1:8000/principal

#127.0.0.1:8000/registro

#127.0.0.1:8000/login

#127.0.0.1:8000/nosotros

#127.0.0.1:8000/Admin

#127.0.0.1:8000/carro

#127.0.0.1:8000/Maui

#127.0.0.1:8000/collokey

