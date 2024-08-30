from django.urls import path

from . import views
from .views import (
    index,
    DishListView,
    DishDetailView,
    CookListView,
    CookDetailView
                    )

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("dishes/<int:pk>", DishDetailView.as_view(), name="dish_detail"),
    path("cooks/", CookListView.as_view(), name="cook_list"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook_detail"),
]

app_name = "catalog"
