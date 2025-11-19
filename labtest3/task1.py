def merge_sort(arr, left=0, right=None):
    """
    Merge Sort algorithm with step-by-step printing
    """
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = (left + right) // 2
        
        # Sort left half
        merge_sort(arr, left, mid)
        
        # Sort right half
        merge_sort(arr, mid + 1, right)
        
        # Merge sorted halves
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    """
    Merge two sorted subarrays and print the step
    """
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    # Merge the two parts
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    
    # Copy remaining elements
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1
    
    # Print merge step
    print(f"Merging {left_part} and {right_part} → {arr[left:right + 1]}")


def main():
    # Prompt user for input (spaces or commas allowed)
    while True:
        s = input("Enter integers separated by spaces or commas: ").strip()
        if not s:
            print("No input provided. Please enter at least one integer.")
            continue
        parts = [p for p in s.replace(",", " ").split() if p]
        try:
            numbers = [int(p) for p in parts]
            break
        except ValueError:
            print("Invalid input. Please enter only integers separated by spaces or commas.")
            continue

    print(f"Original list: {numbers}")
    print("\n--- Merge Sort Steps ---")

    merge_sort(numbers)

    print(f"\nSorted list: {numbers}")


if __name__ == "__main__":
    main()