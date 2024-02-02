from django.shortcuts import render
from .models import Home
from django.http import HttpResponse
from .forms import HomeForm
# Create your views here.
def index(request):
    home_form = HomeForm()
    users = Home.objects.all()
    if(request.method == "POST"):
        email = request.POST['email']
        saran = request.POST['saran']
        print(email, saran)
    #print(request.POST)
    context = {
        'nama': users.get(nama = "John Doe").nama,
        'users': users,
        'judul': 'Home',
        'nav': [
            ['/about', 'about'],
        ],
        'logo': 'Home/image/django logo.png',
        'home_form': home_form,
    }
    return render(request, 'Home/home.html', context)

def angka(request, **input):
    return HttpResponse("<h1>input</h1>" + input['input'])

def slug(request, **input):
    home = Home.objects.get(slug=input)

    nama = "<h1>{}</h1>".format(home.nama)
    slug = "<h1>{}</h1>".format(home.slug)

    return HttpResponse(nama + slug)