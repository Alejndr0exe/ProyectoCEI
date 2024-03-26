from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from intranetApp import forms
from intranetApp.models import Documento, Categoria
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def intranet (request):
    form = forms.addDoc()

    docs = Documento.objects.all()

    if request.method == 'POST':
        form = forms.addDoc(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('intranet'))
        
    context = { 
        'form' : form ,
        'docs' : docs
    }

    return render(request, "intranetApp/intranet.html", context)

@login_required
def script (request):

    categoria_d = Categoria.objects.get(nombre="Scripts")
    scripts = Documento.objects.filter(categoria=categoria_d)

    data = {
        'scripts': scripts
    }

    return render(request, "intranetApp/scrpits.html", data)

@login_required
def manual (request):

    categoria_d = Categoria.objects.get(nombre="Manual")
    manuals = Documento.objects.filter(categoria=categoria_d)

    data = {
        'manuals': manuals
    }

    return render(request, "intranetApp/Manuals.html", data)

@login_required
def protocol (request):

    categoria_d = Categoria.objects.get(nombre="Protocolo")
    protocolos = Documento.objects.filter(categoria=categoria_d)

    data = {
        'protocolos': protocolos
    }

    return render(request, "intranetApp/protocol.html", data)

@login_required
def data (request):

    categoria_d = Categoria.objects.get(nombre="Datos")
    datos = Documento.objects.filter(categoria=categoria_d)

    data = {
        'datos': datos
    }

    return render(request, "intranetApp/data.html", data)


@login_required
def eliminarDoc(request, id):
    doc = get_object_or_404(Documento, id=id)
    doc.delete()
    return HttpResponseRedirect(reverse('intranet'))

