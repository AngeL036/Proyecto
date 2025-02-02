from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fk = models.ForeignKey('Publicacion',
                           on_delete=models.CASCADE)
    def __str__(self):
        return f"Perfil de {self.user.username}"
    
class Publicacion(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Publicacion de {self.usuario.username} - {self.fecha_creacion}"
    
    
