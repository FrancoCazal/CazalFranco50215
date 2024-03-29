from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

# Página Principal

def home(request):
    return render(request, "aplicacion/index.html")

# Funciones para Recetas Saladas
class SaladaList(LoginRequiredMixin, ListView):
    model = Salada
    template_name = 'aplicacion/listaSaladas.html'

@login_required
def createSalada(request):
    if request.method == 'POST':
        miForm = SaladaForm(request.POST, request.FILES)
        if miForm.is_valid():
        # Se envian los datos a través de un formulario POST
            salada_usuario = User.objects.get(username=request.user)
            salada_titulo = miForm.cleaned_data.get('titulo')
            salada_tipo = miForm.cleaned_data.get('tipo')
            salada_ocasion = miForm.cleaned_data.get('ocasion')
            salada_ingredientes = miForm.cleaned_data.get('ingredientes')
            salada_preparacion = miForm.cleaned_data.get('preparacion')
            salada_imagen = miForm.cleaned_data.get('imagenRecetaSalada')
        
        # Creamos el objeto y asignamos el usuario actual
            receta = Salada(usuario=salada_usuario,
                            titulo=salada_titulo,
                            tipo=salada_tipo,
                            ocasion=salada_ocasion,
                            ingredientes=salada_ingredientes,
                            preparacion=salada_preparacion,
                            imagenRecetaSalada=salada_imagen)
            receta.save()
            return redirect(reverse_lazy("listaSaladas"))
        
        # Redireccionamos a la lista después de crear el objeto
    else:
        miForm = SaladaForm()
    return render(request, "aplicacion/createSalada.html", {"form": miForm})

class SaladaDetalle(LoginRequiredMixin, DetailView):
    model = Salada
    context_object_name = 'salada'
    template_name = 'aplicacion/detalleSalada.html'

class SaladaUpdate(LoginRequiredMixin, UpdateView):
    model = Salada
    fields = ["titulo", "tipo", "ocasion", "ingredientes", "preparacion", "imagenRecetaSalada"]
    template_name = 'aplicacion/updateSalada.html'
    success_url = reverse_lazy("listaSaladas")

class SaladaDelete(LoginRequiredMixin, DeleteView):
    model = Salada
    template_name = 'aplicacion/deleteSalada.html'
    success_url = reverse_lazy("listaSaladas")

# Funciones para Recetas Dulces
class DulceList(LoginRequiredMixin, ListView):
    model = Dulce
    template_name = 'aplicacion/listaDulces.html'

@login_required
def createDulce(request):
    if request.method == 'POST':
        miForm = DulceForm(request.POST, request.FILES)
        if miForm.is_valid():
        # Se envian los datos a través de un formulario POST
            dulce_usuario = User.objects.get(username=request.user)
            dulce_titulo = miForm.cleaned_data.get('titulo')
            dulce_tipo = miForm.cleaned_data.get('tipo')
            dulce_ocasion = miForm.cleaned_data.get('ocasion')
            dulce_ingredientes = miForm.cleaned_data.get('ingredientes')
            dulce_preparacion = miForm.cleaned_data.get('preparacion')
            dulce_imagen = miForm.cleaned_data.get('imagenRecetaDulce')
        
        # Creamos el objeto y asignamos el usuario actual
            receta = Dulce(usuario=dulce_usuario,
                           titulo=dulce_titulo,
                           tipo=dulce_tipo,
                           ocasion=dulce_ocasion,
                           ingredientes=dulce_ingredientes,
                           preparacion=dulce_preparacion,
                           imagenRecetaDulce=dulce_imagen)
            receta.save()
            return redirect(reverse_lazy("listaDulces"))
        
        # Redireccionamos a la lista después de crear el objeto
    else:
        miForm = DulceForm()
    return render(request, "aplicacion/createDulce.html", {"form": miForm})

class DulceDetalle(LoginRequiredMixin, DetailView):
    model = Dulce
    context_object_name = 'dulce'
    template_name = 'aplicacion/detalleDulce.html'

class DulceUpdate(LoginRequiredMixin, UpdateView):
    model = Dulce
    fields = ["titulo", "tipo", "ocasion", "ingredientes", "preparacion", "imagenRecetaDulce"]
    template_name = 'aplicacion/updateDulce.html'
    success_url = reverse_lazy("listaDulces")

class DulceDelete(LoginRequiredMixin, DeleteView):
    model = Dulce
    template_name = 'aplicacion/deleteDulce.html'
    success_url = reverse_lazy("listaDulces")

# Funciones para Recetas de Bebidas
class BebidaList(LoginRequiredMixin, ListView):
    model = Bebida
    template_name = 'aplicacion/listaBebidas.html'

@login_required
def createBebida(request):
    if request.method == 'POST':
        miForm = BebidaForm(request.POST, request.FILES)
        if miForm.is_valid():
        # Se envian los datos a través de un formulario POST
            bebida_usuario = User.objects.get(username=request.user)
            bebida_titulo = miForm.cleaned_data.get('titulo')
            bebida_tipo = miForm.cleaned_data.get('tipo')
            bebida_ocasion = miForm.cleaned_data.get('ocasion')
            bebida_ingredientes = miForm.cleaned_data.get('ingredientes')
            bebida_preparacion = miForm.cleaned_data.get('preparacion')
            bebida_imagen = miForm.cleaned_data.get('imagenRecetaBebida')
        
        # Creamos el objeto y asignamos el usuario actual
            receta = Bebida(usuario=bebida_usuario,
                            titulo=bebida_titulo,
                            tipo=bebida_tipo,
                            ocasion=bebida_ocasion,
                            ingredientes=bebida_ingredientes,
                            preparacion=bebida_preparacion,
                            imagenRecetaBebida=bebida_imagen)
            receta.save()
            return redirect(reverse_lazy("listaBebidas"))
        
        # Redireccionamos a la lista después de crear el objeto
    else:
        miForm = BebidaForm()
    return render(request, "aplicacion/createBebida.html", {"form": miForm})

class BebidaDetalle(LoginRequiredMixin, DetailView):
    model = Bebida
    context_object_name = 'bebida'
    template_name = 'aplicacion/detalleBebida.html'

class BebidaUpdate(LoginRequiredMixin, UpdateView):
    model = Bebida
    fields = ["titulo", "tipo", "ocasion", "ingredientes", "preparacion", "imagenRecetaBebida"]
    template_name = 'aplicacion/updateBebida.html'
    success_url = reverse_lazy("listaBebidas")

class BebidaDelete(LoginRequiredMixin, DeleteView):
    model = Bebida
    template_name = 'aplicacion/deleteBebida.html'
    success_url = reverse_lazy("listaBebidas")

# Funciones para los articulos del Blog
class ArticuloList(LoginRequiredMixin, ListView):
    model = Articulo
    template_name = 'aplicacion/listaArticulos.html'

@login_required
def createArticulo(request):
    if request.method == 'POST':
        miForm = ArticuloForm(request.POST, request.FILES)
        if miForm.is_valid():
        # Se envian los datos a través de un formulario POST
            articulo_usuario = User.objects.get(username=request.user)
            articulo_titulo = miForm.cleaned_data.get('titulo')
            articulo_subtitulo = miForm.cleaned_data.get('subtitulo')
            articulo_contenido = miForm.cleaned_data.get('contenido')
            articulo_imagen = miForm.cleaned_data.get('imagen')
        
        # Creamos el objeto y asignamos el usuario actual
            articulo = Articulo(usuario=articulo_usuario,
                                titulo=articulo_titulo,
                                subtitulo=articulo_subtitulo,
                                contenido=articulo_contenido,
                                imagen=articulo_imagen)
            articulo.save()
            return redirect(reverse_lazy("listaArticulos"))
        
        # Redireccionamos a la lista después de crear el objeto
    else:
        miForm = ArticuloForm()
    return render(request, "aplicacion/createArticulo.html", {"form": miForm})

class ArticuloDetalle(LoginRequiredMixin, DetailView):
    model = Articulo
    context_object_name = 'articulo'
    template_name = 'aplicacion/detalleArticulo.html'

class ArticuloUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ["titulo", "subtitulo", "contenido", "imagen"]
    template_name = 'aplicacion/updateArticulo.html'
    success_url = reverse_lazy("listaArticulos")

class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    template_name = 'aplicacion/deleteArticulo.html'
    success_url = reverse_lazy("listaArticulos")

# Funciones para Login, Logout y Registro
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            # Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            return render(request, "aplicacion/index.html")        
        else:
            return redirect(reverse_lazy('login'))
            
    else:
        miForm = AuthenticationForm()
        # Se envia formulario vacio al cliente y se renderiza
    return render(request, "aplicacion/login.html", {"form": miForm})

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("login"))

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()
    return render(request, "aplicacion/registro.html", {"form": miForm})

# Funciones para Edicion de Perfil, Cambio de Clave y Agregar Avatar
@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiarClave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        # Se recuperan los daos no binarios (POST) y binarios (FILES)
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            # Se lee para verificar si hay avatares pertenecientes al usuario
            avatarViejo = Avatar.objects.filter(user=usuario)
            # Borrar avatares viejos (rutas)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            # Agregar el nuevo avatar (se guarda en media)
            avatar = Avatar(user=usuario, imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            # Se crea una variable con la ruta de la imagen
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            print(f"{imagen}")
            return redirect(reverse_lazy('home'))
    else:
        miForm = AvatarForm()
    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm})

# Acerca de Mi
@login_required
def acercaDeMi(request):
    return render(request, "aplicacion/acercaDeMi.html")

# Acerca del Sitio
@login_required
def acercaDelSitio(request):
    return render(request, "aplicacion/acercaDelSitio.html")

# Búsqueda de Recetas
@login_required
def buscarRecetas(request):
    return render(request, "aplicacion/buscarRecetas.html")

@login_required
def encontrarRecetas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        saladas = Salada.objects.filter(titulo__icontains=patron)
        dulces = Dulce.objects.filter(titulo__icontains=patron)
        bebidas = Bebida.objects.filter(titulo__icontains=patron)
        contexto = {"salada_list": saladas, "dulce_list": dulces, "bebida_list": bebidas}
        return render(request, "aplicacion/listaRecetas.html", contexto)
    
    contexto = {'salada_list':Salada.objects.all(),'dulce_list':Dulce.objects.all(), 'bebida_list':Bebida.objects.all()}
    return render(request, "aplicacion/pagina.html", contexto)

# Búsqueda de Artículos
@login_required
def buscarArticulos(request):
    return render(request, "aplicacion/buscarArticulos.html")

@login_required
def encontrarArticulos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        articulos =  Articulo.objects.filter(titulo__icontains=patron)
        contexto = {"articulo_list": articulos}
        return render(request, "aplicacion/listaArticulos.html", contexto)
    
    contexto = {'articulo_list':Articulo.objects.all()}
    return render(request, "aplicacion/pagina.html", contexto)

# Lista de Recetas
@login_required
def listaRecetas(request):
    contexto = {'salada_list':Salada.objects.all(),'dulce_list':Dulce.objects.all(), 'bebida_list':Bebida.objects.all()}
    return render(request, "aplicacion/listaRecetas.html", contexto)