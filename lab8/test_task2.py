import unittest
from task2 import assign_grade
class TestAssignGrade(unittest.TestCase):
    def test_assign_grade(self):
        test_cases = [
            (100, "A"),
            (95, "A"),
            (90, "A"),
            (89, "B"),
            (85, "B"),
            (80, "B"),
            (79, "C"),
            (75, "C"),
            (70, "C"),
            (69, "D"),
            (65, "D"),
            (60, "D"),
            (59, "F"),
            (0, "F"),
            (50, "F"),
            (-1, "Invalid input"),
            (101, "Invalid input"),
            ("eighty", "Invalid input"),
            (None, "Invalid input"),
            ([80], "Invalid input"),
        ]
        for score, expected in test_cases:
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), expected)
if __name__ == "__main__":
    unittest.main()