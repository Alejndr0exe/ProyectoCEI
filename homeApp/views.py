from django.shortcuts import render
from newsPortal.models import Noticias

# Create your views here.
def index(request):

    news = Noticias.objects.all()
    data = {
        'news' : news
    }

    return render(request,"homeApp/index.html", data)
