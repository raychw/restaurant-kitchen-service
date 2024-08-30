from django.urls import path

from . import views
from .views import index, DishListView

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish_list"),
]

app_name = "catalog"
