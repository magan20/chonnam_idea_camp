import os

from django.shortcuts import render, redirect
from django.http import HttpResponse

from culture_circle_api.models import Category, Show


def main(request):
    show_list = Show.objects.all()
    content = {
        "show_list": show_list,
    }
    return render(request, "app/info.html", content)


def detail(request, show_id):
    show = Show.objects.get(id=show_id)
    img_path = show.poster_dir_path
    img_link_list = os.listdir(img_path)
    content = {
        "show": show,
        "poster_path": img_link_list[0],
        "img_link_list": img_link_list[1:],
    }
    return render(request, "app/show_detail.html", content)


def register(request):
    pass


def show_list(request):
    pass


def local(request):
    pass
