import os
from django.shortcuts import render, redirect
from . models import *


def home(r):
    search = r.GET.get('search')
    if search:
        prof = Update.objects.filter(name__icontains=search)
    else:
        prof = Update.objects.all()
    return render(r, 'home.html', locals())


def create(r):
    if r.method == 'POST':
        name = r.POST['name']
        email = r.POST['email']
        image = r.FILES['image']
        prof = Update.objects.create(name=name, email=email, image=image)
        prof.save()
        return redirect('home')
    return render(r, 'create.html', locals())


def update(r, id):
    prof = Update.objects.get(id=id)
    if r.method == 'POST':
        name = r.POST['name']
        email = r.POST['email']
        image = r.FILES.get('image')
        if len(r.FILES) != 0:
            if len(prof.image) > 0:
                os.remove(prof.image.path)
            prof.image = image
        prof.name = name
        prof.email = email
        prof.save()
        return redirect('home')
    return render(r, 'update.html', locals())


def delete(r, id):
    prof = Update.objects.get(id=id)
    if len(prof.image) > 0:
        os.remove(prof.image.path)
        prof.delete()
        return redirect('home')
    prof = Update.objects.all()
    return render(r, 'home.html', locals())
