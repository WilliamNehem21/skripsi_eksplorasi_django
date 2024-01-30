from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul': 'About',
        'nav': [
            ['/home', 'home'],
            ['/about/aboutUs', 'about us'] ],
    }
    return render(request, 'About/about.html', context)

def aboutUS(request):
    return render(request, 'aboutUs.html')