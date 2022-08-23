from django.db import models

# Create your models here.


class Show(models.Model):
    title = models.CharField(max_length=100)
    poster_dir_path = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    runtime = models.IntegerField(blank=False)
    min_price = models.IntegerField(blank=False)
    max_price = models.IntegerField(blank=False)
