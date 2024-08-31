from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import DishForm
from catalog.models import Dish, Cook, DishType


def index(request):
    """View function for the home page of the site."""

    num_dish_types = DishType.objects.all().count()
    num_dishes = Dish.objects.all().count()
    num_cooks = Cook.objects.all().count()

    num_visits = request.session.get("num_visits", 0)
    num_visits += 1
    request.session["num_visits"] = num_visits

    context = {
        "num_dish_types": num_dish_types,
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_visits": num_visits,
    }

    return render(request, "catalog/index.html", context=context)


class DishListView(generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "catalog/dish_list.html"


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(generic.edit.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("catalog:dish_list")


class CookListView(generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "catalog/cook_list.html"


class CookDetailView(generic.DetailView):
    model = Cook


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "catalog/dish_type_list.html"
