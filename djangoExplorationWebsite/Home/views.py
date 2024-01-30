from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'nama': 'John Doe',
        'judul': 'Home',
        'nav': [
            ['/about', 'about'],
        ],
    }
    return render(request, 'Home/home.html', context)