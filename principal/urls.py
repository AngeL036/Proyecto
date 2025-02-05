
from django.urls import path
from .views import index,Registro,login_view,logout_view,crear_publicacion,pantalla,perfil
urlpatterns = [
    path('', index,name='index'),
    path('Registro/', Registro, name='Registro'),
    path('login/',login_view,name='login_view'),
    path('logout/',logout_view,name='logout_view'),
    path('crear_publicacion/',crear_publicacion,name='crear_publicacion'),
    path('pantalla/',pantalla,name='pantalla'),
    path('perfil/<str:username>/',perfil,name='perfil'),
]