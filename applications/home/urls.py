# creamos el archivo urls aqui
from django.urls import path
from . import views

urlpatterns = [
    # mandar a llamar al archivo vistas
    path('home/', views.PruebaView.as_view() ),
]