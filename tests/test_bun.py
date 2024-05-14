from fixtures import sesame_bun_data, sample_bun, modified_bun, bun_data, standard_bun_data

class TestBun:
    def test_get_name(self, sample_bun, standard_bun_data):
        assert sample_bun["name"] == standard_bun_data["name"]

    def test_get_price(self, sample_bun, standard_bun_data):
        assert sample_bun["price"] == standard_bun_data["price"]

    def test_initialization(self, sample_bun, standard_bun_data):
        assert sample_bun == standard_bun_data

    def test_set_name(self, modified_bun, sesame_bun_data):
        modified_bun["name"] = sesame_bun_data["name"]
        assert modified_bun["name"] == sesame_bun_data["name"]

    def test_set_price(self, modified_bun, sesame_bun_data):
        modified_bun["price"] = sesame_bun_data["price"]
        assert modified_bun["price"] == sesame_bun_data["price"]




