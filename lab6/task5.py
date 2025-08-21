
# Function-based approach to create a simple account
def create_account(name, balance=0):
    # Returns a dictionary representing a simple account
    return {"name": name, "balance": balance}

# Function to deposit money into the dictionary-based account
def deposit(account, amount):
    if amount > 0:
        account["balance"] += amount   # Increase balance
        print(f"Deposited: {amount}. New Balance: {account['balance']}")
    else:
        print("Deposit amount must be positive.")

class BankAccount:
    # Constructor to initialize account with name and balance
    def __init__(self, name, balance=0):   
        self.name = name
        self.balance = balance

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount   # Add to balance
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount   # Deduct from balance
                print(f"Withdrew: {amount}. New Balance: {self.balance}")
            else:
                print("Insufficient funds.")   # Cannot withdraw more than balance
        else:
            print("Withdrawal amount must be positive.")

    # Method to display and return current balance
    def get_balance(self):
        print(f"Current Balance: {self.balance}")
        return self.balance

if __name__ == "__main__":   
    # Get account holder's name from user
    name = input("Enter account holder's name: ")
    try:
        # Try to take an initial balance from user
        balance = float(input("Enter initial balance: "))
    except ValueError:
        # If invalid input, set balance = 0
        print("Invalid balance. Setting balance to 0.")
        balance = 0

    # Create an account object using the BankAccount class
    account = BankAccount(name, balance)
    print(f"Account created for {account.name} with balance {account.balance}")

    # Menu-driven program loop for user interaction
    while True:
        print("\nOptions: 1) Deposit 2) Withdraw 3) Balance 4) Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # Deposit option
            try:
                amt = float(input("Enter amount to deposit: "))
                account.deposit(amt)
            except ValueError:
                print("Invalid amount.")

        elif choice == "2":
            # Withdraw option
            try:
                amt = float(input("Enter amount to withdraw: "))
                account.withdraw(amt)
            except ValueError:
                print("Invalid amount.")

        elif choice == "3":
            # Check balance
            account.get_balance()

        elif choice == "4":
            # Exit program
            print("Exiting.")
            break

        else:
            # Invalid menu choice
            print("Invalid option.")
