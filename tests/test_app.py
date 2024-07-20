import unittest
import json
import os
from app import (is_unique_combination,
                 find_minimal_unique_combination,
                 serialize_to_csv, main
                 )


class TestFunctions(unittest.TestCase):
    """
    Класс для тестирования функций модуля app.
    """

    def setUp(self):
        """
        Метод, вызываемый перед каждым тестом.
        """
        self.data = [
            {
                "фамилия": "Смирнов",
                "имя": "Евгений",
                "отчество": "Александрович",
                "класс": "6",
                "подгруппа": "1",
                "предмет": "История",
                "видДеятельности": "Учебная",
                "количествоЧасовВнеделю": "2"
            },
            {
                "фамилия": "Смирнов",
                "имя": "Евгений",
                "отчество": "Александрович",
                "класс": "7",
                "предмет": "История",
                "видДеятельности": "Учебная",
                "количествоЧасовВнеделю": "2"
            },
            {
                "фамилия": "Смирнов",
                "имя": "Евгений",
                "отчество": "Александрович",
                "класс": "8",
                "предмет": "История",
                "видДеятельности": "Учебная",
                "количествоЧасовВнеделю": "2"
            }
        ]

        self.priority = [
            "фамилия", "имя", "отчество", "класс", "подгруппа", "предмет",
            "видДеятельности", "количествоЧасовВнеделю"
        ]

    def tearDown(self):
        """
        Метод, вызываемый после каждого теста.
        Удаляет временные файлы, созданные во время тестов.
        """
        if os.path.exists('test_data.json'):
            os.remove('test_data.json')

    def test_is_unique_combination(self):
        """
        Тестирует функцию is_unique_combination.
        """
        self.assertTrue(is_unique_combination(self.data, ["класс"]))
        self.assertFalse(is_unique_combination(self.data, ["фамилия"]))

    def test_find_minimal_unique_combination(self):
        """
        Тестирует функцию find_minimal_unique_combination.
        """
        self.assertEqual(
            find_minimal_unique_combination(self.data, self.priority),
            ["класс"]
        )

    def test_serialize_to_csv(self):
        """
        Тестирует функцию serialize_to_csv.
        """
        columns = ["класс"]
        expected_csv = "Минимальный уникальный идентификатор\nкласс"
        self.assertEqual(serialize_to_csv(columns), expected_csv)

    def test_main_function(self):
        """
        Тестирует основную функцию main.
        """
        json_data = json.dumps(self.data, ensure_ascii=False)
        json_file_path = 'test_data.json'
        with open(json_file_path, 'w', encoding='utf-8') as file:
            file.write(json_data)

        expected_csv = "Минимальный уникальный идентификатор\nкласс"
        self.assertEqual(main(json_file_path), expected_csv)


if __name__ == '__main__':
    unittest.main()
