from django.urls import path

from . import views
from .views import (
    index,
    DishListView,
    DishDetailView,
    CookListView,
    CookDetailView,
    DishTypeListView,
    DishCreateView,
    CookCreateView,
    DishTypeCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("dishes/<int:pk>", DishDetailView.as_view(), name="dish_detail"),
    path("cooks/", CookListView.as_view(), name="cook_list"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook_detail"),
    path("dish_types/", DishTypeListView.as_view(), name="dish_type_list"),
    path("dishes/create", DishCreateView.as_view(), name="dish_create"),
    path("cooks/create", CookCreateView.as_view(), name="cook_create"),
    path("dish_types/create", DishTypeCreateView.as_view(), name="dish_type_create"),
]

app_name = "catalog"
