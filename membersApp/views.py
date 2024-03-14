from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from membersApp import forms

# Create your views here.

def miembros(request):
    return render(request,"members/members.html")

def addMiembro(request):
    form = forms.addMember()

    if request.method == 'POST':
        form = forms.addMember(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('addMember'))


    context = {'form': form }

    return render(request, "members/addMembers.html", context)
