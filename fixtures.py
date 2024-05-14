import pytest
from praktikum.ingredient import Ingredient

@pytest.fixture
def ingredient_class():
    return Ingredient

@pytest.fixture
def ingredient(request):
    # Возвращаем заранее определенный ингредиент для тестов
    return Ingredient("Sauce", "Mayonnaise", 0.2)

@pytest.fixture(params=[
    ("Sauce", "Ketchup", 0.1),
    ("Filling", "Cheese", 0.5),
    ("Sauce", "Mustard", 0.15),
])
def ingredient_data(request):
    return request.param

@pytest.fixture
def expected_price():
    return 0.2

@pytest.fixture
def bun_data():
    return {
        "standard": {"name": "Standard Bun", "price": 1.5},
        "sesame": {"name": "Sesame Bun", "price": 2.0}
    }

@pytest.fixture
def sample_bun(bun_data):
    return bun_data["standard"]

@pytest.fixture
def modified_bun(bun_data):
    return bun_data["sesame"]

@pytest.fixture
def sesame_bun_data(bun_data):
    return bun_data["sesame"]

@pytest.fixture
def standard_bun_data(bun_data):
    return bun_data["standard"]