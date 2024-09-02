from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from catalog.models import Cook, Dish, DishType, Ingredient


class LoginTestCase(TestCase):
    def test_login_required(self):
        res = self.client.get(reverse("catalog:index"))
        self.assertNotEqual(res.status_code, 200)


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass"
        )
        self.client.login(
            username="testuser",
            password="testpass"
        )

    @classmethod
    def setUpTestData(cls):
        DishType.objects.create(
            name="Pasta",
        )
        Cook.objects.create(
            username="reichikku",
            first_name="Slawa",
            last_name="Melnyk",
            years_of_experience="1",
        )
        Dish.objects.create(
            name="Pasta Carbonara",
            description="Delicious Italian pasta",
            price=119.99,
            dish_type=DishType.objects.get(name="Pasta"),
        )
        Ingredient.objects.create(
            name="Garlic",
        )


class IndexViewTest(BaseTestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("catalog:index"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("catalog:index"))
        self.assertTemplateUsed(response, "catalog/index.html")

    def test_context_data(self):
        response = self.client.get(reverse("catalog:index"))
        self.assertEqual(
            response.context["num_cooks"],
            Cook.objects.count()
        )
        self.assertEqual(
            response.context["num_dishes"],
            Dish.objects.count()
        )
        self.assertEqual(
            response.context["num_dish_types"],
            DishType.objects.count()
        )


class DishTypeListViewTest(BaseTestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("catalog:dish_type_list"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("catalog:dish_type_list"))
        self.assertTemplateUsed(response, "catalog/dish_type_list.html")

    def test_search_functionality(self):
        response = self.client.get(
            reverse("catalog:dish_type_list"),
            {"name": "Pasta"}
        )
        self.assertContains(response, "Pasta")

    def setUp(self):
        super().setUp()
        DishType.objects.create(name="Breakfast")
        DishType.objects.create(name="Main Course")
        DishType.objects.create(name="Soup")

    def test_search_returns_correct_results(self):
        response = self.client.get(
            reverse("catalog:dish_type_list"),
            {"name": "Main Course"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Main Course")
        self.assertNotContains(response, "Breakfast")
        self.assertNotContains(response, "Soup")

    def test_search_returns_all_if_no_query(self):
        response = self.client.get(reverse("catalog:dish_type_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Main Course")
        self.assertContains(response, "Breakfast")
        self.assertContains(response, "Soup")


class CookListViewTest(BaseTestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("catalog:cook_list"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("catalog:cook_list"))
        self.assertTemplateUsed(response, "catalog/cook_list.html")

    def test_search_functionality(self):
        response = self.client.get(
            reverse("catalog:cook_list"),
            {"username": "reichikku"}
        )
        self.assertContains(response, "reichikku")


class DishListViewTest(BaseTestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("catalog:dish_list"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("catalog:dish_list"))
        self.assertTemplateUsed(response, "catalog/dish_list.html")

    def test_search_functionality(self):
        response = self.client.get(
            reverse("catalog:dish_list"),
            {"name": "Pasta Carbonara"}
        )
        self.assertContains(response, "Pasta Carbonara")


class IngredientListViewTest(BaseTestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("catalog:ingredient_list"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("catalog:ingredient_list"))
        self.assertTemplateUsed(response, "catalog/ingredient_list.html")

    def test_search_functionality(self):
        response = self.client.get(
            reverse("catalog:ingredient_list"),
            {"name": "Garlic"}
        )
        self.assertContains(response, "Garlic")

    def setUp(self):
        super().setUp()
        Ingredient.objects.create(name="Onion")
        Ingredient.objects.create(name="Butter")
        Ingredient.objects.create(name="Milk")

    def test_search_returns_correct_results(self):
        response = self.client.get(
            reverse("catalog:ingredient_list"),
            {"name": "Milk"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Milk")
        self.assertNotContains(response, "Onion")
        self.assertNotContains(response, "Butter")

    def test_search_returns_all_if_no_query(self):
        response = self.client.get(reverse("catalog:ingredient_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Onion")
        self.assertContains(response, "Butter")
        self.assertContains(response, "Milk")
