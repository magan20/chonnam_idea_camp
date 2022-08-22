from django.shortcuts import render
from django.http import HttpResponse


def index(requests):
    return HttpResponse("this is culter_circle page")
