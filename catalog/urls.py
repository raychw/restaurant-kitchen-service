from django.urls import path

from . import views
from .views import (
    index,
    DishListView,
    DishDetailView,
                    )

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("dishes/<int:pk>", DishDetailView.as_view(), name="dish_detail"),
]

app_name = "catalog"
