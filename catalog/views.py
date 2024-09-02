from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.forms import DishForm, CookCreationForm, DishNameSearchForm, CookUsernameSearchForm, \
    DishTypeNameSearchForm, IngredientNameSearchForm
from catalog.models import Dish, Cook, DishType, Ingredient


@login_required
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


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "catalog/dish_list.html"

    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["search_form"] = DishNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        form = DishNameSearchForm(self.request.GET)
        queryset = Dish.objects.select_related("dish_type")

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("catalog:dish_list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("catalog:dish_list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("catalog:dish_list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "catalog/cook_list.html"

    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")

        context["search_form"] = CookUsernameSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        form = CookUsernameSearchForm(self.request.GET)
        queryset = Cook.objects.all()

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = (
        "first_name",
        "last_name",
        "email"
    )
    success_url = reverse_lazy("catalog:cook_list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("catalog:cook_list")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "catalog/dish_type_list.html"

    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["search_form"] = DishTypeNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        form = DishTypeNameSearchForm(self.request.GET)
        queryset = DishType.objects.all()

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "catalog/dish_type_form.html"
    success_url = reverse_lazy("catalog:dish_type_list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "catalog/dish_type_form.html"
    success_url = reverse_lazy("catalog:dish_type_list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "catalog/dish_type_confirm_delete.html"
    success_url = reverse_lazy("catalog:dish_type_list")


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    context_object_name = "ingredient_list"
    template_name = "catalog/ingredient_list.html"

    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["search_form"] = IngredientNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        form = IngredientNameSearchForm(self.request.GET)
        queryset = Ingredient.objects.all()

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    template_name = "catalog/ingredient_form.html"
    success_url = reverse_lazy("catalog:ingredient_list")


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    template_name = "catalog/ingredient_form.html"
    success_url = reverse_lazy("catalog:ingredient_list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    template_name = "catalog/ingredient_confirm_delete.html"
    success_url = reverse_lazy("catalog:ingredient_list")




@login_required
def toggle_assign_to_dish(request, pk):
    cook = Cook.objects.get(id=request.user.id)
    if (
        Dish.objects.get(id=pk) in cook.dishes.all()
    ):
        cook.dishes.remove(pk)
    else:
        cook.dishes.add(pk)
    return HttpResponseRedirect(reverse_lazy("catalog:dish_detail", args=[pk]))
