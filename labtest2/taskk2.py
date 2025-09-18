"""
List Comparison: Added and Removed Items
========================================

This program compares two lists of lines and returns the added and removed items
while preserving the display order. Uses sets for efficiency but maintains
stable ordering via list comprehensions.

Author: AI Assistant
"""

def compare_lists(old, new):
    """
    Compare two lists and return added and removed items preserving order.
    
    Args:
        old (list): Original list of lines
        new (list): New list of lines
        
    Returns:
        tuple: (added, removed) where both are lists preserving original order
    """
    # Convert to sets for efficient lookup
    old_set = set(old)
    new_set = set(new)
    
    # Find added items (in new but not in old) - preserve new list order
    added = [item for item in new if item not in old_set]
    
    # Find removed items (in old but not in new) - preserve old list order
    removed = [item for item in old if item not in new_set]
    
    return added, removed


def print_comparison_result(old, new, added, removed):
    """Helper function to display comparison results in a readable format."""
    print("\n" + "=" * 60)
    print("LIST COMPARISON RESULTS")
    print("=" * 60)
    
    print(f"\nOriginal list ({len(old)} items):")
    for i, item in enumerate(old, 1):
        print(f"  {i:2}. {item}")
    
    print(f"\nNew list ({len(new)} items):")
    for i, item in enumerate(new, 1):
        print(f"  {i:2}. {item}")
    
    print(f"\nAdded items ({len(added)} items):")
    if added:
        for i, item in enumerate(added, 1):
            print(f"  {i:2}. + {item}")
    else:
        print("  (none)")
    
    print(f"\nRemoved items ({len(removed)} items):")
    if removed:
        for i, item in enumerate(removed, 1):
            print(f"  {i:2}. - {item}")
    else:
        print("  (none)")
    
    print("\n" + "=" * 60)


def get_lists_from_user():
    """
    Get two lists from user input for comparison.
    
    Returns:
        tuple: (old_list, new_list)
    """
    print("\nEnter the original list:")
    print("(Enter one item per line, press Enter twice when done)")
    old_list = []
    while True:
        item = input().strip()
        if item == "":
            break
        old_list.append(item)
    
    print("\nEnter the new list:")
    print("(Enter one item per line, press Enter twice when done)")
    new_list = []
    while True:
        item = input().strip()
        if item == "":
            break
        new_list.append(item)
    
    return old_list, new_list


def test_list_comparison():
    """Comprehensive test cases for list comparison."""
    print("=" * 60)
    print("TESTING LIST COMPARISON")
    print("=" * 60)
    
    # Test Case 1: Basic addition and removal
    print("\nTest 1: Basic addition and removal")
    old1 = ["apple", "banana", "cherry"]
    new1 = ["banana", "date", "elderberry"]
    added1, removed1 = compare_lists(old1, new1)
    print_comparison_result(old1, new1, added1, removed1)
    
    expected_added1 = ["date", "elderberry"]
    expected_removed1 = ["apple", "cherry"]
    assert added1 == expected_added1, f"Test 1 added failed: expected {expected_added1}, got {added1}"
    assert removed1 == expected_removed1, f"Test 1 removed failed: expected {expected_removed1}, got {removed1}"
    print("✓ Test 1 passed")
    
    # Test Case 2: No changes
    print("\nTest 2: No changes")
    old2 = ["a", "b", "c"]
    new2 = ["a", "b", "c"]
    added2, removed2 = compare_lists(old2, new2)
    print_comparison_result(old2, new2, added2, removed2)
    
    expected_added2 = []
    expected_removed2 = []
    assert added2 == expected_added2, f"Test 2 added failed: expected {expected_added2}, got {added2}"
    assert removed2 == expected_removed2, f"Test 2 removed failed: expected {expected_removed2}, got {removed2}"
    print("✓ Test 2 passed")
    
    # Test Case 3: Only additions
    print("\nTest 3: Only additions")
    old3 = ["x", "y"]
    new3 = ["x", "y", "z", "w"]
    added3, removed3 = compare_lists(old3, new3)
    print_comparison_result(old3, new3, added3, removed3)
    
    expected_added3 = ["z", "w"]
    expected_removed3 = []
    assert added3 == expected_added3, f"Test 3 added failed: expected {expected_added3}, got {added3}"
    assert removed3 == expected_removed3, f"Test 3 removed failed: expected {expected_removed3}, got {removed3}"
    print("✓ Test 3 passed")
    
    
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED! ✓")
    print("=" * 60)


def main():
    """Main function to run the list comparison program."""
    print("LIST COMPARISON: ADDED AND REMOVED ITEMS")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Run tests")
        print("2. Compare your own lists")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            test_list_comparison()
        
        elif choice == "2":
            try:
                old_list, new_list = get_lists_from_user()
                added, removed = compare_lists(old_list, new_list)
                print_comparison_result(old_list, new_list, added, removed)
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
