from praktikum.ingredient import Ingredient

class TestBurger:

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients

    def test_move_ingredient(self, burger, ingredient):
        ingredient1 = Ingredient("Lettuce", "Filling", 0.5)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient1)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient1, ingredient]

    def test_get_price(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == bun.get_price() * 2 + ingredient.get_price()

    def test_get_receipt_contains_bun_name(self, burger, bun, ingredient):
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        assert bun.get_name() in receipt

    def test_get_receipt_contains_ingredient_name(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        assert ingredient.get_name() in receipt

    def test_get_receipt_contains_price(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        assert str(burger.get_price()) in receipt
