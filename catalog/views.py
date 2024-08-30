from django.shortcuts import render
from django.views import generic

from catalog.models import Dish, Cook, DishType


def index(request):
    """View function for the home page of the site."""

    num_dish_types = DishType.objects.all().count()
    num_dishes = Dish.objects.all().count()
    num_cooks = Cook.objects.all().count()

    context = {
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
    }

    return render(request, "catalog/index.html", context=context)


class DishListView(generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "catalog/dish_list.html"


class DishDetailView(generic.DetailView):
    model = Dish


class CookListView(generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "catalog/cook_list.html"


class CookDetailView(generic.DetailView):
    model = Cook
