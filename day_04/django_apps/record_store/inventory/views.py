from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from inventory.models import * 
from .forms import AlbumForm


def index(request):
    artists = Artist.objects.all()

    return render(request, "inventory/index.html", locals())

@login_required
def album_new(request):
    if request.method == "POST": 
        form = AlbumForm(request.POST) 
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('index')
    else:
        form=AlbumForm()
        return render(request, "inventory/album_form.html", {'form': form})

