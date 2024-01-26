from django.shortcuts import render

# Create your views here.

def miembros(request):
    return render(request,"members/members.html")