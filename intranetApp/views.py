from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from intranetApp import forms
from intranetApp.models import Script, Data, Manual
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def intranet (request):
    return render(request, "intranetApp/intranet.html")

@login_required
def script (request):
    scripts = Script.objects.all()
    data = {
        'scripts' : scripts
    }
    
    return render(request, "intranetApp/scrpits.html", data)


@login_required
def addScript (request):
    form = forms.addScript()

    if request.method == 'POST':
        form = forms.addScript(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('script'))


    context = {'form': form }

    return render(request, "intranetApp/addScript.html", context)

@login_required
def eliminarScript(request, id):
    script = get_object_or_404(Script, id=id)
    script.delete()
    return HttpResponseRedirect(reverse('script'))







@login_required
def data (request):

    datas = Data.objects.all()
    data = {
        'datas' : datas
    }
    
    return render(request, "intranetApp/data.html", data)

@login_required
def addData (request):
    form = forms.addData()

    if request.method == 'POST':
        form = forms.addData(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('data'))


    context = {'form': form }

    return render(request, "intranetApp/addData.html", context)

@login_required
def eliminarData(request, id):
    data = get_object_or_404(Data, id=id)
    data.delete()
    return HttpResponseRedirect(reverse('data'))







@login_required
def manual (request):
    manuals = Manual.objects.all()
    data = {
        'manuals' : manuals
    }
    
    return render(request, "intranetApp/Manuals.html", data)

@login_required
def addManual (request):
    form = forms.addManual()

    if request.method == 'POST':
        form = forms.addManual(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manuals'))


    context = {'form': form }

    return render(request, "intranetApp/addManual.html", context)


@login_required
def eliminarManual(request, id):
    manual = get_object_or_404(Manual, id=id)
    manual.delete()
    return HttpResponseRedirect(reverse('manuals'))