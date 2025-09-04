import string
def is_sentence_palindrome(sentence: str) -> bool:
    """
    Checks if a sentence is a palindrome, ignoring case, spaces, and punctuation.
    """
    # Remove punctuation and spaces, convert to lowercase
    cleaned = ''.join(
        ch.lower() for ch in sentence if ch.isalnum()
    )
    return cleaned == cleaned[::-1]
# Test cases
if __name__ == "__main__":
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
        result = is_sentence_palindrome(sentence)
        print(f"'{sentence}' -> {result} (Expected: {expected})")