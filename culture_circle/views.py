import os

from django.shortcuts import render, redirect
from django.http import HttpResponse

from culture_circle_api.models import Category, Show, RegistShow, Article


def main(request):
    recommend_show_list = Show.objects.all().order_by("like")[:4]
    show_list = Show.objects.all()
    content = {
        "recommend_show_list": recommend_show_list,
        "show_list": show_list,
    }
    return render(request, "app/local.html", content)


def detail(request, show_id):
    show = Show.objects.get(id=show_id)
    img_path = show.poster_dir_path
    img_link_list = os.listdir(img_path)
    img_link_list.sort()
    content = {
        "show": show,
        "img_link_list": img_link_list,
    }
    return render(request, "app/show_detail.html", content)


def register(request):
    if request.method == "GET":
        return render(request, "app/show_register_page.html")
    else:
        print(request.POST)
        title = request.POST["title"]
        category = request.POST["category"]
        region = request.POST["region"]
        start_date = request.POST["start_date"]
        end_date = request.POST["end_date"]
        runtime = int(request.POST["runtime"])
        price = int(request.POST["price"])
        description = request.POST["description"]

        try:
            category = Category.objects.get(name=category)
        except:
            category = Category.objects.create(name=category)

        RegistShow.objects.create(
            title=title,
            link="",
            category=category,
            region=region,
            start_date=start_date,
            end_date=end_date,
            runtime=runtime,
            min_price=price,
            max_price=price,
            description=description,
        )

        return render(request, "app/redirect.html")


def show_list(request):
    return render(request, "app/info.html")


def local(request):
    pass
