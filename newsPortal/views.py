from django.shortcuts import render
from newsPortal.models import Noticias

# Create your views here.
def newsPortal(request):
    news = Noticias.objects.all()
    data = {
        'news' : news
    }

    return render(request,"news/news.html", data) 

def newCei (request, id):
    new = Noticias.objects.get (id = id)
    data = {
        'new' : new
    }

    return render(request, "news/new.html", data)