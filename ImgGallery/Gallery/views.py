from django.shortcuts import render
from .forms import ImageForm
from django.http import HttpResponse
from.models import Images

# Create your views here.
def images(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
    
def imag(request,gen):
    pics = None
    dta=None
    pics = Images.objects.all()
    if gen == 'games':
        g = 'Games'
        dta = Images.objects.filter(genre='Games').count()
        if dta:
            is_there = True
        else:
            is_there = False
    elif gen == 'nature':
        g = 'Nature'
        dta = Images.objects.filter(genre='Nature').count()
        if dta:
            is_there = True
        else:
            is_there = False
    elif gen == 'celebs':
        g = 'Celebrities'
        dta = Images.objects.filter(genre='Celebrities').count()
        if dta:
            is_there = True
        else:
            is_there = False
    cont = {'img': pics, 'there': is_there, 'gen': g}
    return render(request, 'every.html', cont)

def trial(request, gen):
    msg = "Running trial"
    return HttpResponse(msg)


