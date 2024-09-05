from django.urls import path

from catalog.views import (
    index,
    DishListView,
    DishDetailView,
    CookListView,
    CookDetailView,
    DishTypeListView,
    DishCreateView,
    CookCreateView,
    DishTypeCreateView,
    DishUpdateView,
    DishDeleteView,
    CookUpdateView,
    CookDeleteView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    toggle_assign_to_dish,
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish_detail"),
    path("cooks/", CookListView.as_view(), name="cook_list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook_detail"),
    path("dish_types/", DishTypeListView.as_view(), name="dish_type_list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish_create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish_update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish_delete"),
    path("cooks/create/", CookCreateView.as_view(), name="cook_create"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook_update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook_delete"),
    path("dish_types/create/", DishTypeCreateView.as_view(), name="dish_type_create"),
    path("dish_types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish_type_update"),
    path("dish_types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish_type_delete"),
    path("dishes/<int:pk>/toggle_assign/", toggle_assign_to_dish, name="toggle_dish_assign"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient_list"),
    path("ingredients/create/", IngredientCreateView.as_view(), name="ingredient_create"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(), name="ingredient_update"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredient_delete"),
]

app_name = "catalog"
