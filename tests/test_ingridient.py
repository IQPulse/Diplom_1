from fixtures import ingredient_class, ingredient, ingredient_data, expected_price

class TestIngredient:
    def test_ingredient_attributes(self, ingredient_class, ingredient_data):
        ingredient_type, name, price = ingredient_data
        ingredient_instance = ingredient_class(ingredient_type, name, price)
        assert ingredient_instance.type == ingredient_type
        assert ingredient_instance.name == name
        assert ingredient_instance.price == price

    def test_get_price(self, ingredient, expected_price):
        assert ingredient.get_price() == expected_price

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == "Mayonnaise"

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == "Sauce"

    def test_get_type_filling(self, ingredient):
        ingredient.type = "Filling"
        assert ingredient.get_type() == "Filling"
