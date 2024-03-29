from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Salada, Dulce, Bebida, Post

class Salada(models.Model):
    recetaSaladaTipo = (
        ('Plato Principal','Plato Principal'),
        ('Entrada','Entrada'),
        ('Snack','Snack'),     
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=recetaSaladaTipo, default='snack')
    ocasion = models.CharField(max_length=20)
    ingredientes = models.TextField(null=True, blank=True)
    preparacion = models.TextField(null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    imagenRecetaSalada = models.ImageField(upload_to="galeria", null=True)
    def __str__(self):
        return f"{self.titulo}"
    
class Dulce(models.Model):
    recetaDulceTipo = (
        ('Postre','Postre'),
        ('Snack','Snack'),     
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=recetaDulceTipo, default='snack')
    ocasion = models.CharField(max_length=20)
    ingredientes = models.TextField(null=True, blank=True)
    preparacion = models.TextField(null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    imagenRecetaDulce = models.ImageField(upload_to="galeria", null=True)
    def __str__(self):
        return f"{self.titulo}"
    
class Bebida(models.Model):
    recetaBebidaTipo = (
        ('Con Alcohol','Con Alcohol'),
        ('Sin Alcohol','Sin Alcohol'),
        ('Cafetería','Cafetería'),  
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=recetaBebidaTipo, default='sinAlcohol')
    ocasion = models.CharField(max_length=20)
    ingredientes = models.TextField(null=True, blank=True)
    preparacion = models.TextField(null=True, blank=True)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    imagenRecetaBebida = models.ImageField(upload_to="galeria", null=True)
    def __str__(self):
        return f"{self.titulo}"
    
class Articulo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    contenido = models.TextField(null=True)
    fechaPublicacion = models.DateField(auto_now_add=True, auto_now=False)
    imagen = models.ImageField(upload_to="galeria", null=True)
    def __str__(self):
        return f"{self.titulo}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares/", default="media/avatares/default.jpg")
    # Si se elimina un user, el avatar del user se elimina
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"