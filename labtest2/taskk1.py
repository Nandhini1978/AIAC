"""
Matrix Rotation 90° Clockwise
=============================

This program rotates an NxN matrix 90 degrees clockwise in-place.
Uses the transpose + reverse approach for efficiency.

Author: AI Assistant
"""
def rotate_matrix_90_clockwise(matrix):
    """
    Rotate an NxN matrix 90 degrees clockwise in-place.
    
    Algorithm: Transpose + Reverse each row
    Time Complexity: O(N²)
    Space Complexity: O(1) - in-place operation
    
    Args:
        matrix (list): 2D list representing the matrix
        
    Returns:
        list: The rotated matrix (same reference, modified in-place)
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i, n):  # Only iterate upper triangle to avoid double swapping
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
    
    return matrix
def print_matrix(matrix, title="Matrix"):
    """Helper function to print matrix in a readable format."""
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(f"{val:3}" for val in row))
    print()
def get_matrix_from_user():
    """
    Get matrix size and values from user input.
    
    Returns:
        list: 2D list representing the matrix
    """
    while True:
        try:
            n = int(input("Enter the size of the NxN matrix (N): "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    print(f"\nEnter {n}x{n} matrix values (row by row):")
    matrix = []
    
    for i in range(n):
        while True:
            try:
                row_input = input(f"Row {i+1} (enter {n} space-separated integers): ")
                row = list(map(int, row_input.split()))
                
                if len(row) != n:
                    print(f"Please enter exactly {n} integers.")
                    continue
                
                matrix.append(row)
                break
            except ValueError:
                print("Please enter valid integers separated by spaces.")
    
    return matrix
def test_matrix_rotation():
    """Comprehensive test cases for matrix rotation."""
    print("=" * 50)
    print("TESTING MATRIX ROTATION")
    print("=" * 50)
    
    # Test Case 1: 1x1 matrix
    print("\nTest 1: 1x1 Matrix")
    matrix1 = [[5]]
    print_matrix(matrix1, "Original")
    rotate_matrix_90_clockwise(matrix1)
    print_matrix(matrix1, "Rotated 90°")
    expected1 = [[5]]
    assert matrix1 == expected1, f"Test 1 failed: expected {expected1}, got {matrix1}"
    print("✓ Test 1 passed")
    
    # Test Case 2: 2x2 matrix
    print("\nTest 2: 2x2 Matrix")
    matrix2 = [[1, 2], [3, 4]]
    print_matrix(matrix2, "Original")
    rotate_matrix_90_clockwise(matrix2)
    print_matrix(matrix2, "Rotated 90°")
    expected2 = [[3, 1], [4, 2]]
    assert matrix2 == expected2, f"Test 2 failed: expected {expected2}, got {matrix2}"
    print("✓ Test 2 passed")
    
    # Test Case 3: 3x3 matrix (from sample)
    print("\nTest 3: 3x3 Matrix")
    matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix(matrix3, "Original")
    rotate_matrix_90_clockwise(matrix3)
    print_matrix(matrix3, "Rotated 90°")
    expected3 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert matrix3 == expected3, f"Test 3 failed: expected {expected3}, got {matrix3}"
    print("✓ Test 3 passed")
    print("\n" + "=" * 50)
    print("ALL TESTS PASSED! ✓")
    print("=" * 50)
def main():
    """Main function to run the matrix rotation program."""
    print("MATRIX ROTATION 90° CLOCKWISE")
    print("=" * 40)
    while True:
        print("\nChoose an option:")
        print("1. Run tests")
        print("2. Rotate your own matrix")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            test_matrix_rotation()
        
        elif choice == "2":
            try:
                matrix = get_matrix_from_user()
                print_matrix(matrix, "Your Original Matrix")
                rotate_matrix_90_clockwise(matrix)
                print_matrix(matrix, "Rotated 90° Clockwise")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()
