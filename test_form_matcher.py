import unittest
from form_matcher import find_template

class TestFormMatcher(unittest.TestCase):
    def test_match_template(self):
        templates = [
            {"name": "Test", "login": "email", "tel": "phone"}
        ]
        query = {
            "login": "talyadukhovna7@gmail.com",
            "tel": "+7 999 999 99 99"
        }
        self.assertEqual(find_template(query, templates), "Test")

    def test_no_match(self):
        templates = [
            {"name": "Test", "login": "email", "tel": "phone"}
        ]
        query = {
            "name": "Talya",
            "date": "24.24.2024"
        }
        self.assertEqual(find_template(query, templates), {"name": "text", "date": "date"})

    def test_extra_fields_in_query(self):
        templates = [
            {"name": "Test", "login": "email"}
        ]
        query = {
            "login": "info@example.com",
            "extra": "value"
        }
        self.assertEqual(find_template(query, templates), "Test")

    def test_incorrect_phone_format(self):
        templates = [
            {"name": "Test", "tel": "phone"}
        ]
        query = {
            "tel":"666666666"
        }
        self.assertEqual(find_template(query, templates), {"tel": "text"})

    def test_iso_date_format(self):
        templates = [
            {"name": "Test", "birthdate": "date"}
        ]
        query = {
            "birthdate": "1993-07-01"
        }
        self.assertEqual(find_template(query, templates), "Test")

    def test_template_without_name_is_ignored(self):
        templates = [
            {"login": "email"} 
        ]
        query = {
            "login": "info@example.com"
        }
        self.assertEqual(find_template(query, templates), {"login": "email"})

if __name__ == 'main':
    unittest.main()