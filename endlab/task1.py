from collections import defaultdict
from typing import Iterable, Tuple, Any, Dict
import math
import unittest

"""
task1.py

Purpose:
    Provide a small, well-documented Python implementation that finds the
    highest-rated product from a list of rating events. This file also
    contains an "effective zero-shot prompt" (string) that can be fed to an
    LLM to generate the same functionality, plus unit tests.

Behavior:
    - Input: an iterable of (product_id, rating) pairs where:
        * product_id is any hashable identifier (str, int, etc.)
        * rating is numeric (int/float)
    - Output: a dict with keys:
        * 'product_id'      : the winning product id
        * 'average_rating'  : average rating (float)
        * 'num_reviews'     : number of ratings considered for that product
    - Tie-breaking:
        1) Higher average rating wins.
        2) If average ratings tie within floating epsilon, the product with more reviews wins.
        3) If still tied, deterministic fallback: min(product_id) by natural ordering.
    - Errors:
        * Raises ValueError for empty input or if no valid numeric ratings are found.

Zero-shot prompt:
    The PROMPT variable below contains an effective zero-shot prompt you can give
    to a capable code generation model to produce this implementation (including
    docs, comments, and tests).
"""


# An effective zero-shot prompt to generate the functionality in this file.
PROMPT = """
Implement a Python function `highest_rated_product(ratings)` that:
- Accepts `ratings`: an iterable of pairs (product_id, rating).
  * product_id: any hashable identifier (string or integer recommended).
  * rating: numeric value (int or float). Ignore non-numeric ratings.
- Computes the average rating per product.
- Returns a dict: {
    'product_id': best_id,
    'average_rating': best_avg (float),
    'num_reviews': count_for_best
  }
- Tie-breaking rules:
  1) Higher average rating wins.
  2) If averages are equal within floating-point tolerance, the product with more reviews wins.
  3) If still tied, pick the deterministic minimum product_id (use Python's natural ordering).
- Validate input:
  * If the input is empty or contains no valid numeric ratings, raise ValueError.
- Include:
  * Clear docstrings and inline comments explaining reasoning.
  * Unit tests covering normal cases, ties, and error cases.
  * A small complexity note: O(n) time, O(k) space where k is number of distinct products.
- Use only Python standard library constructs.
"""

# ---- Implementation ----

def highest_rated_product(ratings: Iterable[Tuple[Any, float]]) -> Dict[str, Any]:
    """
    Find the product with the highest average rating.

    Args:
        ratings: Iterable of pairs (product_id, rating). Non-numeric ratings are ignored.

    Returns:
        A dict with keys:
            - 'product_id': identifier of the best product
            - 'average_rating': average rating as float
            - 'num_reviews': number of ratings for that product

    Raises:
        ValueError: if `ratings` is empty or no valid numeric ratings are found.
    Complexity:
        O(n) time where n is the number of rating entries; O(k) space for k distinct products.
    """
    sums = defaultdict(float)   # product_id -> sum of ratings
    counts = defaultdict(int)   # product_id -> count of ratings

    seen_any = False
    for entry in ratings:
        # Expect pairs; be robust to sequences/tuples
        try:
            pid, score = entry
        except Exception:
            # Ignore malformed entries
            continue
        # Accept numeric ratings (int/float). Reject NaN and non-numeric.
        if isinstance(score, (int, float)) and not (isinstance(score, float) and math.isnan(score)):
            sums[pid] += float(score)
            counts[pid] += 1
            seen_any = True
        else:
            # ignore non-numeric or NaN values
            continue

    if not seen_any:
        raise ValueError("No valid numeric ratings provided.")

    # Compute averages and determine best product using tie-breakers
    best_pid = None
    best_avg = -math.inf
    best_count = -1
    EPS = 1e-9

    for pid in counts:
        avg = sums[pid] / counts[pid]
        cnt = counts[pid]
        # Compare averages with tolerance
        if (avg > best_avg + EPS) or \
           (abs(avg - best_avg) <= EPS and cnt > best_count) or \
           (abs(avg - best_avg) <= EPS and cnt == best_count and (best_pid is None or pid < best_pid)):
            best_pid = pid
            best_avg = avg
            best_count = cnt

    return {
        'product_id': best_pid,
        'average_rating': float(best_avg),
        'num_reviews': int(best_count)
    }

# ---- Tests ----

class TestHighestRatedProduct(unittest.TestCase):
    def test_simple(self):
        ratings = [
            ('A', 4.5),
            ('B', 3.0),
            ('A', 5.0),
            ('B', 4.0),
            ('C', 5.0)
        ]
        result = highest_rated_product(ratings)
        # Averages: A=(4.5+5.0)/2=4.75, B=(3+4)/2=3.5, C=5.0
        # C has highest average (1 review)
        self.assertEqual(result['product_id'], 'C')
        self.assertAlmostEqual(result['average_rating'], 5.0)
        self.assertEqual(result['num_reviews'], 1)

    def test_tie_break_by_count(self):
        ratings = [
            ('X', 5.0),
            ('Y', 5.0),
            ('Y', 5.0),
            ('Z', 5.0)
        ]
        # All averages equal 5.0, Y has 2 reviews so should win
        result = highest_rated_product(ratings)
        self.assertEqual(result['product_id'], 'Y')
        self.assertAlmostEqual(result['average_rating'], 5.0)
        self.assertEqual(result['num_reviews'], 2)

    def test_tie_break_by_id(self):
        ratings = [
            (2, 4.0),
            (1, 4.0)
        ]
        # Both average 4.0 and same count; pick min id => 1
        result = highest_rated_product(ratings)
        self.assertEqual(result['product_id'], 1)
        self.assertEqual(result['num_reviews'], 1)

    def test_ignores_non_numeric_and_malformed(self):
        ratings = [
            ('A', 4.0),
            ('A', 'bad'),
            ('B', float('nan')),
            ('B', 5.0),
            ('C',)  # malformed entry should be ignored
        ]
        # A average 4.0 (1), B average 5.0 (1) -> B wins
        result = highest_rated_product(ratings)
        self.assertEqual(result['product_id'], 'B')
        self.assertAlmostEqual(result['average_rating'], 5.0)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            highest_rated_product([])

    def test_all_invalid_raises(self):
        with self.assertRaises(ValueError):
            highest_rated_product([('a', 'x'), ('b', None)])

if __name__ == "__main__":
    # Run the unit tests when executed directly.
    unittest.main(verbosity=2)