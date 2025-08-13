def register_user():
    print("\n=== User Registration ===")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    print(f"Registration successful!\nUsername: {username}\nPassword: {password}")
    return username, password

def login_user(registered_username, registered_password):
    print("\n=== User Login ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == registered_username and password == registered_password:
        print("Login successful!")
        # After successful login, offer to update registration (linking logic)
        update = input("Do you want to update your registration details? (yes/no): ").strip().lower()
        if update == 'yes':
            new_username, new_password = register_user()
            print("Your registration details have been updated. Please login again with new credentials.")
            return new_username, new_password
    else:
        print("Login failed. Invalid username or password.")
    return registered_username, registered_password

def main():
    registered_username = None
    registered_password = None
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            registered_username, registered_password = register_user()
        elif choice == '2':
            if registered_username is None or registered_password is None:
                print("No user registered yet. Please register first.")
            else:
                registered_username, registered_password = login_user(registered_username, registered_password)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()