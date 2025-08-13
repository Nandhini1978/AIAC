def get_numbers():
    nums = input("Enter numbers separated by spaces: ")
    try:
        num_list = [int(x) for x in nums.strip().split()]
        return num_list
    except ValueError:
        print("Invalid input. Please enter only integers.")
        return get_numbers()

def sort_menu():
    print("\nMenu:")
    print("1. Sort all numbers in ascending order")
    print("2. Sort all numbers in descending order")
    print("3. Sort odd numbers in ascending order")
    print("4. Sort even numbers in descending order")
    print("5. Exit")

def main():
    numbers = get_numbers()
    while True:
        sort_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            sorted_nums = sorted(numbers)
            print("Numbers in ascending order:", sorted_nums)
        elif choice == '2':
            sorted_nums = sorted(numbers, reverse=True)
            print("Numbers in descending order:", sorted_nums)
        elif choice == '3':
            odd_nums = [n for n in numbers if n % 2 != 0]
            sorted_odds = sorted(odd_nums)
            print("Odd numbers in ascending order:", sorted_odds)
        elif choice == '4':
            even_nums = [n for n in numbers if n % 2 == 0]
            sorted_evens = sorted(even_nums, reverse=True)
            print("Even numbers in descending order:", sorted_evens)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
