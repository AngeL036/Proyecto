
from django.urls import path
from .views import index,Registro,login_view,logout_view
urlpatterns = [
    path('', index,name='index'),
    path('Registro/', Registro, name='Registro'),
    path('login/',login_view,name='login_view'),
    path('logout/',logout_view,name='logout_view'),
]