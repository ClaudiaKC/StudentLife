from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_evenimente, name='lista_evenimente'),  # Ruta principala pentru evenimente
]
