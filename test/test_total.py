from unittest import TestCase
from unittest.mock import patch

import set_test_path
import numbers_to_add
from app import create_app

class TestTotal(TestCase):
    def setUp(self):
        self.app = create_app()

    @patch("numbers_to_add._get_numbers_to_add")
    def test_logic_1(self, mock_numbers):
        mock_numbers.return_value = [3, 66, 1]
        response = self.app.test_client().get("/total")
        assert response.json == {"total": 70}

    @patch("numbers_to_add._get_numbers_to_add")
    def test_logic_2(self, mock_numbers):
        mock_numbers.return_value = [3, -66]
        response = self.app.test_client().get("/total")
        assert response.json == {"total": -63}
