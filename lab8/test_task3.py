import unittest
from task3 import is_sentence_palindrome

class TestIsSentencePalindrome(unittest.TestCase):
    def test_is_sentence_palindrome(self):
        test_cases = [
            ("A man a plan a canal Panama", True),
            ("No lemon, no melon", True),
            ("Was it a car or a cat I saw?", True),
            ("Hello, World!", False),
            ("", True),
            ("Able was I, I saw Elba", True),
            ("Not a palindrome", False),
            ("Eva, can I see bees in a cave?", True),
            ("Madam In Eden, I'm Adam", True),
            ("Step on no pets", True),
        ]
        for sentence, expected in test_cases:
            with self.subTest(sentence=sentence):
                self.assertEqual(is_sentence_palindrome(sentence), expected)

if __name__ == "__main__":
    unittest.main()