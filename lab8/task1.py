def is_valid_email(email: str) -> bool:
    # Must contain exactly one '@'
    if email.count('@') != 1:
        return False
    # Must contain at least one '.'
    if '.' not in email:
        return False
    # Must not start or end with '.' or '@'
    if email[0] in {'.', '@'} or email[-1] in {'.', '@'}:
        return False
    return True

def validator():
    email = input("Enter your email address: ")
    if is_valid_email(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

if __name__ == "__main__":
    validator()