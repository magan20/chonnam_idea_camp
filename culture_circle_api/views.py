from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from datetime import datetime

from .models import Show, Category
from .serializers import ShowGetSerializer, ShowCreateSerializer, CategoryGetSerializer, CategoryCreateSerializer

# Create your views here.


class CategoriesAPI(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryGetSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryAPI(APIView):
    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        serializer = CategoryGetSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        serializer = CategoryCreateSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return Response(dict(OK=True), status=status.HTTP_200_OK)


class ShowsAPI(APIView):
    def get(self, request):
        shows = Show.objects.all()
        serializer = ShowGetSerializer(shows, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShowAPI(APIView):
    def get(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        serializer = ShowGetSerializer(show)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        serializer = ShowCreateSerializer(show, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        show.delete()
        return Response(dict(OK=True), status=status.HTTP_200_OK)


def create_a_show(request):
    if request.method == "GET":
        content = {}
        try:
            content["file_cnt"] = int(request.GET["file_cnt"]) or 0
        except:
            content["file_cnt"] = 0
        return render(request, "api/create_show.html", content)
    else:
        title = request.POST["title"]
        link = request.POST["link"]
        category_name = request.POST["category"]
        region = request.POST["region"]
        start_date = datetime.strptime(request.POST["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(request.POST["end_date"], "%Y-%m-%d")
        runtime = int(request.POST["runtime"])
        min_price = int(request.POST["min_price"])
        max_price = int(request.POST["max_price"])

        try:
            category = Category.objects.get(name=category_name)
        except:
            category = Category.objects.create(name=category_name)

        show = Show.objects.create(
            title=title,
            link=link,
            category=category,
            region=region,
            start_date=start_date,
            end_date=end_date,
            runtime=runtime,
            min_price=min_price,
            max_price=max_price,
        )

        show_id = show.id
        poster_dir_path = f"static/img/{show_id}/"

        Show.objects.filter(id=show_id).update(poster_dir_path=poster_dir_path)

        cnt = 1
        while f"image_{cnt}" in request.FILES:
            image_file = request.FILES[f"image_{cnt}"]
            fs = FileSystemStorage(location=poster_dir_path, base_url=poster_dir_path)
            fs.save(f"image_{cnt}", image_file)
            cnt += 1

        return redirect("show_create")
