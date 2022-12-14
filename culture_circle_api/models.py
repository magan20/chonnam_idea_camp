from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Show(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    poster_dir_path = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    runtime = models.IntegerField(blank=False)
    min_price = models.IntegerField(blank=False)
    max_price = models.IntegerField(blank=False)
    like = models.IntegerField(blank=True)


class RegistShow(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    poster_dir_path = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    runtime = models.IntegerField(blank=False)
    min_price = models.IntegerField(blank=False)
    max_price = models.IntegerField(blank=False)


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=200)
    poster_dir_path = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
