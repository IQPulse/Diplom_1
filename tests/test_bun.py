class TestBun:
    def test_get_name(self, sample_bun):
        assert sample_bun.get_name() == "Standard Bun"

    def test_get_price(self, sample_bun):
        assert sample_bun.get_price() == 1.5

    def test_initialization(self, sample_bun):
        assert sample_bun.__dict__ == {
            "name": "Standard Bun",
            "price": 1.5
        }

    def test_set_name(self, sample_bun):
        bun = sample_bun
        bun.name = "Sesame Bun"
        assert bun.name == "Sesame Bun"

    def test_set_price(self, sample_bun):
        bun = sample_bun
        bun.price = 2.0
        assert bun.price == 2.0


