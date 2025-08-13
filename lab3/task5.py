def convert_temperature():
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    def celsius_to_kelvin(c):
        return c + 273.15

    def kelvin_to_celsius(k):
        return k - 273.15

    def fahrenheit_to_kelvin(f):
        return (f - 32) * 5/9 + 273.15

    def kelvin_to_fahrenheit(k):
        return (k - 273.15) * 9/5 + 32

    while True:
        print("\nTemperature Conversion Menu:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            try:
                c = float(input("Enter temperature in Celsius: "))
                f = celsius_to_fahrenheit(c)
                print(f"{c:.2f}°C = {f:.2f}°F")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '2':
            try:
                f = float(input("Enter temperature in Fahrenheit: "))
                c = fahrenheit_to_celsius(f)
                print(f"{f:.2f}°F = {c:.2f}°C")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '3':
            try:
                c = float(input("Enter temperature in Celsius: "))
                k = celsius_to_kelvin(c)
                print(f"{c:.2f}°C = {k:.2f}K")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '4':
            try:
                k = float(input("Enter temperature in Kelvin: "))
                c = kelvin_to_celsius(k)
                print(f"{k:.2f}K = {c:.2f}°C")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '5':
            try:
                f = float(input("Enter temperature in Fahrenheit: "))
                k = fahrenheit_to_kelvin(f)
                print(f"{f:.2f}°F = {k:.2f}K")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '6':
            try:
                k = float(input("Enter temperature in Kelvin: "))
                f = kelvin_to_fahrenheit(k)
                print(f"{k:.2f}K = {f:.2f}°F")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == '7':
            print("Exiting temperature conversion menu.")
            break
        else:
            print("Invalid choice. Please select a valid option (1-7).")

if __name__ == "__main__":
    convert_temperature()
