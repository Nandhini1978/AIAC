def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        print("Currency not supported.")
        return None
    # Convert amount to base currency (e.g., USD), then to target currency
    base_amount = amount / rates[from_currency]
    converted = base_amount * rates[to_currency]
    return converted

# Example exchange rates (relative to USD)
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.92,
    'GBP': 0.78,
    'INR': 83.0,
    'JPY': 157.0
}

# Get user input
amount = float(input("Enter amount: "))
from_currency = input("Convert from (currency code): ").upper()
to_currency = input("Convert to (currency code): ").upper()

result = convert_currency(amount, from_currency, to_currency, exchange_rates)
if result is not None:
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")