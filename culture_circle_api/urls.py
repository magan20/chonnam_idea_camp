from django.urls import path

from .views import CategoriesAPI, CategoryAPI, ShowsAPI, ShowAPI, create_a_show

urlpatterns = [
    path("categories/", CategoriesAPI.as_view(), name="categories"),
    path("category/<int:category_id>", CategoryAPI.as_view(), name="category"),
    path("shows/", ShowsAPI.as_view(), name="shows"),
    path("show/", create_a_show, name="show_create"),
    path("show/<int:show_id>", ShowAPI.as_view(), name="show"),
]
