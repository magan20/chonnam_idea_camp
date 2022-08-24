from rest_framework import serializers
from .models import Show, Category


class ShowGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = [
            "id",
            "poster_dir_path",
            "title",
            "category",
            "region",
            "start_date",
            "end_date",
            "runtime",
            "min_price",
            "max_price",
        ]


class ShowCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = ["title", "category", "region", "start_date", "end_date", "runtime", "min_price", "max_price"]


class CategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
