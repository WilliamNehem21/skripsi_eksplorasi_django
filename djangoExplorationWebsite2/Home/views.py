from django.shortcuts import render
from .models import Home

# Create your views here.
def index(request):
    users = Home.objects.all()
    context = {
        'nama': users.get(nama = "John Doe").nama,
        'users': users,
        'judul': 'Home',
        'nav': [
            ['/about', 'about'],
        ],
        'logo': 'Home/image/django logo.png',
    }
    return render(request, 'Home/home.html', context)