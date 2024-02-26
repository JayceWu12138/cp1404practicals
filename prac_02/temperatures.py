def main():
    print("Temperature Converter")
    choice = input("Convert from (C)elsius or (F)ahrenheit? ").upper()
    if choice == 'C':
        celsius = float(input("Celsius temperature: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"Result: {celsius} C = {fahrenheit:.2f} F")
    elif choice == 'F':
        fahrenheit = float(input("Fahrenheit temperature: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"Result: {fahrenheit} F = {celsius:.2f} C")
    else:
        print("Invalid choice")


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


main()
