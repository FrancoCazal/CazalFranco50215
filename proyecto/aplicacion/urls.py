from django.contrib import admin
from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Página Principal
    path('', home, name="home"),

    # URLs para Recetas Saladas
    path('listaSaladas/', SaladaList.as_view(), name="listaSaladas"),
    path('createSalada/', createSalada, name="createSalada"),
    path('detalleSalada/<int:pk>/', SaladaDetalle.as_view(), name="detalleSalada"),
    path('updateSalada/<int:pk>/', SaladaUpdate.as_view(), name="updateSalada"),
    path('deleteSalada/<int:pk>/', SaladaDelete.as_view(), name="deleteSalada"),

    # URLs para Recetas Dulces
    path('listaDulces/', DulceList.as_view(), name="listaDulces"),
    path('createDulce/', createDulce, name="createDulce"),
    path('detalleDulce/<int:pk>/', DulceDetalle.as_view(), name="detalleDulce"),
    path('updateDulce/<int:pk>/', DulceUpdate.as_view(), name="updateDulce"),
    path('deleteDulce/<int:pk>/', DulceDelete.as_view(), name="deleteDulce"),

    # URLs para Recetas de Bebidas
    path('listaBebidas/', BebidaList.as_view(), name="listaBebidas"),
    path('createBebida/', createBebida, name="createBebida"),
    path('detalleBebida/<int:pk>/', BebidaDetalle.as_view(), name="detalleBebida"),
    path('updateBebida/<int:pk>/', BebidaUpdate.as_view(), name="updateBebida"),
    path('deleteBebida/<int:pk>/', BebidaDelete.as_view(), name="deleteBebida"),

    # URLs para Articulos del Blog
    path('listaArticulos/', ArticuloList.as_view(), name="listaArticulos"),
    path('createArticulo/', createArticulo, name="createArticulo"),
    path('detalleArticulo/<int:pk>/', ArticuloDetalle.as_view(), name="detalleArticulo"),
    path('updateArticulo/<int:pk>/', ArticuloUpdate.as_view(), name="updateArticulo"),
    path('deleteArticulo/<int:pk>/', ArticuloDelete.as_view(), name="deleteArticulo"),

    # Login, Logout, Registro
    path('login/', login_request, name="login"),
    path('logout/', logout_view, name="logout"),
    path('registro/', register, name="registro"),

    # Edicion Perfil, Cambio de Clave, Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),

    # Búsqueda
    path('buscarRecetas/', buscarRecetas, name="buscarRecetas"),
    path('encontrarRecetas/', encontrarRecetas, name="encontrarRecetas"),
    path('buscarArticulos/', buscarArticulos, name="buscarArticulos"),
    path('encontrarArticulos/', encontrarArticulos, name="encontrarArticulos"),

    # Otros
    path('listaRecetas/', listaRecetas, name="listaRecetas"),
    path('acercaDeMi/', acercaDeMi, name="acercaDeMi"),
    path('acercaDelSitio/', acercaDelSitio, name="acercaDelSitio"),
    
    ]