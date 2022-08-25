from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.main, name="index"),
    path("shows/", views.show_list, name="list"),
    path("show/", views.register, name="register"),
    path("show/<int:show_id>", views.detail, name="detail"),
    path("local/", views.local, name="local"),
]
