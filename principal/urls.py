
from django.urls import path
from .views import index,Registro
urlpatterns = [
    path('', index,name='index'),
      path("Registro/", Registro, name="Registro"),
]