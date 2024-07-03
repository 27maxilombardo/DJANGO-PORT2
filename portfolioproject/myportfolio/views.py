from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Contacto
from .forms import ContactoForm
# Create your views here.

def home (request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html',{'proyectos':proyectos})

#declarar otras vistas
#VISTA PARA ALMACENAR UN CONTACTO NUEVO 

def contacto_nuevo(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_confirmacion')
        

    else:
        form = ContactoForm()
    return render(request,'myportfolio/contacto_formulario.html', {'form': form})

#Contacto detalle
@login_required
def contacto_detalle(request, pk):
    contacto = get_object_or_404(Contacto,pk=pk)
    return render(request, 'myportfolio/contacto_detalle.html',{'contacto': contacto})

#contacto editar
@login_required
def contacto_editar(request,pk):
    contacto = get_object_or_404(Contacto,pk=pk)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid:
            form.save()
            return redirect('contacto_detalle', pk=contacto.pk)
    else:
        form = ContactoForm(instance=contacto)
    return render(request,'myportfolio/contacto_editar.html',{'form': form})

# declarar mi funcion para eliminar
# ELIMINAR 
@login_required
def contacto_eliminar(request,pk):
    contacto = get_object_or_404(Contacto,pk=pk)
    contacto.delete()
    return redirect('contacto_lista')


#listar los contactos

@login_required
def contacto_listar (request):
    contactos = Contacto.objects.all()
    return render( request, 'myportfolio/contacto_lista.html',{'contactos': contactos})

#confirmacion de todo ok

def contacto_confirmacion (request):
    return render(request, 'myportfolio/contacto_confirmacion.html')

@login_required
def vista_protegida(request):
    return render(request, 'vista_protegida.html')

def proyecto_detalle(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'proyecto_detalle.html', {'proyecto': proyecto})

