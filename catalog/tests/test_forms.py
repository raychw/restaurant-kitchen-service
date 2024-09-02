from django.test import TestCase

from catalog.forms import (
    CookCreationForm,
    CookUsernameSearchForm,
    DishTypeNameSearchForm,
    DishNameSearchForm,
    IngredientNameSearchForm,
)


class FormTests(TestCase):
    def test_cook_username_search_form_is_valid(self):
        form_data = {
            "username": "reichikku",
        }
        form = CookUsernameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_type_name_search_form_is_valid(self):
        form_data = {
            "name": "Pasta",
        }
        form = DishTypeNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_name_search_form_is_valid(self):
        form_data = {
            "name": "Pasta Carbonara",
        }
        form = DishNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_ingredient_name_search_form_is_valid(self):
        form_data = {
            "name": "Garlic",
        }
        form = IngredientNameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_valid_years_of_experience(self):
        form_data = {
            "username": "paiv",
            "first_name": "Vaness",
            "last_name": "Paquet",
            "email": "default@gmail.com",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "years_of_experience": 11
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_years_of_experience_negative_value(self):
        form_data = {
            "username": "qzish",
            "first_name": "Alina",
            "last_name": "Denisiuk",
            "email": "default@gmail.com",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "years_of_experience": -1
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
