def show_previous_bill_receipt(customer_name, customer_id, address, previous_bill):
    print("\n--- Previous Bill Receipt ---")
    print(f"Customer Name     : {customer_name}")
    print(f"Customer ID       : {customer_id}")
    print(f"Address           : {address}")
    print(f"Previous Bill (Rs.): {previous_bill:.2f}")

def calculate_power_bill(units):
    if units <= 100:
        amount = units * 5
    elif units <= 200:
        amount = (100 * 5) + ((units - 100) * 7)
    else:
        amount = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    return amount

def main():
    print("Power Bill Calculator")
    customer_name = input("Enter customer name: ")
    customer_id = input("Enter customer ID: ")
    address = input("Enter customer address: ")
    try:
        units = float(input("Enter number of units consumed: "))
        if units < 0:
            print("Units cannot be negative.")
            return
    except ValueError:
        print("Invalid input for units. Please enter a number.")
        return

    try:
        previous_bill = float(input("Enter previous bill amount (Rs.): "))
        if previous_bill < 0:
            print("Previous bill cannot be negative.")
            return
    except ValueError:
        print("Invalid input for previous bill. Please enter a number.")
        return

    # Show previous bill receipt
    show_previous_bill_receipt(customer_name, customer_id, address, previous_bill)

    bill_amount = calculate_power_bill(units)

    print("\n--- Current Power Bill Details ---")
    print(f"Customer Name     : {customer_name}")
    print(f"Customer ID       : {customer_id}")
    print(f"Address           : {address}")
    print(f"Units Consumed    : {units}")
    print(f"Previous Bill (Rs.): {previous_bill:.2f}")
    print(f"Current Bill (Rs.) : {bill_amount:.2f}")

if __name__ == "__main__":
    main()


