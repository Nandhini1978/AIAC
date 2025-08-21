def sum_to_n_for(n):
    """Calculate sum of first n numbers using a for loop"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_to_n_while(n):
    """Calculate sum of first n numbers using a while loop"""
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


# Main Program
if __name__ == "__main__":
    try:
        n = int(input("Enter a positive integer n: "))
        if n < 0:
            print("Please enter a non-negative number.")
        else:
            print(f"Sum using for loop: {sum_to_n_for(n)}")
            print(f"Sum using while loop: {sum_to_n_while(n)}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
