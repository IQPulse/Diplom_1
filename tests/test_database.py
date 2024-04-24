from unittest.mock import MagicMock

class TestDatabase:
    def test_available_buns(self, database, mock_buns):
        database.available_buns = MagicMock(return_value=mock_buns)
        assert database.available_buns() == mock_buns

    def test_available_ingredients(self, database, mock_ingredients):
        database.available_ingredients = MagicMock(return_value=mock_ingredients)
        assert database.available_ingredients() == mock_ingredients
