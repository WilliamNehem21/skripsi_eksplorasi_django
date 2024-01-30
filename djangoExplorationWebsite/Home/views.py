from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'nama': 'John Doe',
        'judul': 'Home',
        'nav': [
            ['/about', 'about'],
        ],
        'logo': 'Home/image/django logo.png',
    }
    return render(request, 'Home/home.html', context)