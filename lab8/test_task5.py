import unittest
from task5 import convert_date_format
class TestConvertDateFormat(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")
        self.assertEqual(convert_date_format("2000-01-01"), "01-01-2000")
        self.assertEqual(convert_date_format("1999-12-31"), "31-12-1999")

    def test_invalid_format_missing_parts(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-10")
        with self.assertRaises(ValueError):
            convert_date_format("2023")
        with self.assertRaises(ValueError):
            convert_date_format("")

    def test_invalid_format_extra_parts(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-15-01")

    def test_non_numeric_parts(self):
        # The function does not validate numeric values, just the format
        self.assertEqual(convert_date_format("abcd-ef-gh"), "gh-ef-abcd")

if __name__ == "__main__":
    unittest.main()