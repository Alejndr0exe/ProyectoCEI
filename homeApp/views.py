from django.shortcuts import render
from newsPortal.models import News

# Create your views here.
def index(request):

    news = News.objects.all()
    data = {
        'news' : news
    }

    return render(request,"homeApp/index.html", data)
