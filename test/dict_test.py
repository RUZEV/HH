import unittest
from unittest.mock import patch
import requests
import parsHH  # Импорт вашего модуля parsHH

class TestDictProfession(unittest.TestCase):
    @patch('requests.get')
    def test_create_dict(self, mock_get):
        mock_response = [{"specializations": [{"id": 1, "name": "Profession 1"}, {"id": 2, "name": "Profession 2"}]}]
        expected_dict = {1: "Profession 1", 2: "Profession 2"}

        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = mock_response
            result = parsHH.create_dict({})  # Обращение к функции create_dict из parsHH модуля
            self.assertEqual(result, expected_dict)


if __name__ == '__main__':
    unittest.main()