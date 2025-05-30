import unittest
from src.lab7.level3plus.deanon import Deanon

class TestDeanon(unittest.TestCase):
    def setUp(self):
        self.service = Deanon()

    def test_basic_case(self):
        fixture_path = 'tests/lab7/fixtures/01_basic_case.yaml'
        keywords = ["проєкт фенікс", "алгоритм", "астрофотографія", "ябко", "дані"]
        expected_results = {
            "User_TechOleksa": 40.00,
            "User_HobbyistIvanka": 80.00,
            "User_SciFiTaras": 50.00
        }

        results = self.service.analyze(fixture_path, keywords)

        self.assertEqual(len(results), len(expected_results))
        for user, expected_percentage in expected_results.items():
            self.assertIn(user, results)
            self.assertEqual(results[user], expected_percentage)

    def test_complex_case(self):
        fixture_path = 'tests/lab7/fixtures/02_complex_case.yaml'
        keywords = ["проєкт фенікс", "алгоритм", "астрофотографія", "ябко", "123", "дані"]
        expected_results = {
            "User_CasualSofia": 0.00,
            "User_TravelerAndriy": 66.67,
            "User_FoodieOlena": 33.33,
            "User_ProblematicSemen": 16.67,
            "User_EmptyPostsKhrystyna": 0.00,
            "User_NullPostsDmytro": 0.00,
            "User_OnlyNonStringPavlo": 0.00,
            "User_OneEmptyStringMarta": 100.00,
            "User_GenericGrygoriy": 0.00,
            "12345_NumericUser": 66.67
        }

        results = self.service.analyze(fixture_path, keywords)

        self.assertEqual(len(results), len(expected_results))
        for user, expected_percentage in expected_results.items():
            self.assertIn(user, results)
            self.assertEqual(results[user], expected_percentage)

    def test_null_texts_case(self):
        fixture_path = 'tests/lab7/fixtures/03_null_texts_case.yaml'
        keywords = ["проєкт фенікс", "алгоритм", "астрофотографія", "ябко", "123", "дані"]
        expected_results = {
            "UserWithEmptyList": 0.0,
            "UserWithNullTexts": 0.0,
            "UserWithNoTextsField": 0.0,
            "UserWithOneEmptyStringText": 0.0,
            "User_OnlyNonStringValues": 0.0
        }

        results = self.service.analyze(fixture_path, keywords)

        self.assertEqual(len(results), len(expected_results))
        for user, expected_percentage in expected_results.items():
            self.assertIn(user, results)
            self.assertEqual(results[user], expected_percentage)


if __name__ == "__main__":
    unittest.main()
