
from app_cad_usuarios import views
from django.contrib import admin
from django.urls import path

#rota, view responsável, referencia
#index vai vazio no path
urlpatterns = [
        path('', views.home, name='home')  # nome da guia: home
]
