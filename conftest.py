import pytest
from unittest.mock import MagicMock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.burger import Burger

@pytest.fixture
def sample_bun():
    return Bun("Standard Bun", 1.5)

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    return Bun("Burger Bun", 2.0)

@pytest.fixture
def ingredient():
    return Ingredient("Cheese", "Filling")

@pytest.fixture(scope="class")
def ingredient_class():
    return Ingredient("Sauce", "Mayonnaise", 0.2)

@pytest.fixture
def ingredient(ingredient_class):
    return ingredient_class

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def mock_buns():
    bun1 = MagicMock(spec=Bun, name="black bun", weight=100)
    bun2 = MagicMock(spec=Bun, name="white bun", weight=200)
    bun3 = MagicMock(spec=Bun, name="red bun", weight=300)
    return [bun1, bun2, bun3]

@pytest.fixture
def mock_ingredients():
    ingredient1 = MagicMock(spec=Ingredient, name="hot sauce", type="SAUCE", weight=100)
    ingredient2 = MagicMock(spec=Ingredient, name="sour cream", type="SAUCE", weight=200)
    ingredient3 = MagicMock(spec=Ingredient, name="chili sauce", type="SAUCE", weight=300)
    ingredient4 = MagicMock(spec=Ingredient, name="cutlet", type="FILLING", weight=100)
    ingredient5 = MagicMock(spec=Ingredient, name="dinosaur", type="FILLING", weight=200)
    ingredient6 = MagicMock(spec=Ingredient, name="sausage", type="FILLING", weight=300)
    return [ingredient1, ingredient2, ingredient3, ingredient4, ingredient5, ingredient6]
