import pytest
from praktikum.ingredient import Ingredient
class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("Sauce", "Ketchup", 0.1),
        ("Filling", "Cheese", 0.5),
        ("Sauce", "Mustard", 0.15),
    ])
    def test_ingredient_attributes(self, ingredient_class, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == 0.2

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == "Mayonnaise"

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == "Sauce"

    def test_get_type_filling(self, ingredient_class):
        ingredient_class.type = "Filling"
        assert ingredient_class.get_type() == "Filling"


