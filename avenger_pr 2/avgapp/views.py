from django.http import HttpResponse

from .models import Avenger
from django.shortcuts import render, redirect
from .forms import HerosForm

# Create your views here.


def index(request):
    avenger = Avenger.objects.all()
    content = {
        'list':avenger
    }
    return render(request,'index.html',content)


def details(request,avg_id):
    avng = Avenger.objects.get(id=avg_id)
    return render(request,'details.html',{'avng':avng})

def add_hero(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        decs = request.POST.get('decs',)
        img = request.FILES['img']
        hero = Avenger(name=name, decs=decs, img=img)
        hero.save()

    return render(request, 'add.html')

def update(request,id):
    hero= Avenger.objects.get(id=id)
    form = HerosForm(request.POST or None, request.FILES, instance=hero)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'hero':hero})

def delete(request,id):
    if request.method=='POST':
        hero=Avenger.objects.get(id=id)
        hero.delete()
        return redirect('/')
    return    render(request,'delete.html')

