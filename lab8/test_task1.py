import unittest
from task1 import is_valid_email

class TestIsValidEmail(unittest.TestCase):
    def test_is_valid_email(self):
        test_cases = [
            ("user@example.com", True),
            ("user.name@domain.co", True),
            ("user@domain", False),           # No dot
            ("userdomain.com", False),        # No @
            ("user@@domain.com", False),      # Multiple @
            ("user@domain..com", True),       # Double dot allowed by this logic
            (".user@domain.com", False),      # Starts with dot
            ("user.@domain.com", True),       # Dot before @ is allowed
            ("user@domain.com.", False),      # Ends with dot
            ("@userdomain.com", False),       # Starts with @
            ("userdomain.com@", False),       # Ends with @
            ("user@.com", True),              # Dot after @ is allowed
            ("user@domain.c", True),          # Single char TLD
            ("user@domain.c.", False),        # Ends with dot
        ]
        for email, expected in test_cases:
            with self.subTest(email=email):
                self.assertEqual(is_valid_email(email), expected)

if __name__ == "__main__":
    unittest.main()