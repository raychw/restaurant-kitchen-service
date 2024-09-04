from django.test import TestCase
from django.urls import reverse
from catalog.models import (
    DishType,
    Ingredient,
    Dish
)
from django.contrib.auth import get_user_model


class DishTypeModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Pasta")

    def test_dish_type_creation(self):
        self.assertEqual(self.dish_type.name, "Pasta")

    def test_dish_type_str(self):
        self.assertEqual(str(self.dish_type), "Pasta")


class CookModelTest(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(
            username="qzish",
            first_name="Alina",
            last_name="Denisiuk",
            years_of_experience=5,
            password="testpassword123"
        )

    def test_cook_creation(self):
        self.assertEqual(self.cook.username, "qzish")
        self.assertEqual(self.cook.first_name, "Alina")
        self.assertEqual(self.cook.last_name, "Denisiuk")
        self.assertEqual(self.cook.years_of_experience, 5)

    def test_cook_str(self):
        self.assertEqual(str(self.cook), "qzish: Alina Denisiuk")

    def test_get_absolute_url(self):
        self.assertEqual(self.cook.get_absolute_url(), reverse("catalog:cook_detail", kwargs={"pk": self.cook.pk}))


class IngredientModelTest(TestCase):
    def setUp(self):
        self.ingredient = Ingredient.objects.create(name="Garlic")

    def test_ingredient_creation(self):
        self.assertEqual(self.ingredient.name, "Garlic")

    def test_ingredient_str(self):
        self.assertEqual(str(self.ingredient), "Garlic")


class DishModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Course")
        self.cook = get_user_model().objects.create_user(
            username="qzish",
            first_name="ALina",
            last_name="Denisiuk",
            years_of_experience=5,
            password="testpassword123"
        )
        self.ingredient = Ingredient.objects.create(name="Tomato")
        self.dish = Dish.objects.create(
            name="Pasta Carbonara",
            description="Delicious italian pasta",
            price=119.99,
            dish_type=self.dish_type
        )
        self.dish.cooks.add(self.cook)
        self.dish.ingredients.add(self.ingredient)

    def test_dish_creation(self):
        self.assertEqual(self.dish.name, "Pasta Carbonara")
        self.assertEqual(self.dish.description, "Delicious italian pasta")
        self.assertEqual(self.dish.price, 119.99)
        self.assertEqual(self.dish.dish_type, self.dish_type)

    def test_dish_str(self):
        self.assertEqual(str(self.dish), "Pasta Carbonara")

    def test_dish_cooks_relationship(self):
        self.assertIn(self.cook, self.dish.cooks.all())

    def test_dish_ingredients_relationship(self):
        self.assertIn(self.ingredient, self.dish.ingredients.all())
