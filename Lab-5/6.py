# 6.	Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.
def fahrenheit_to_celsius():
    fahrenheit_temps = [32, 50, 77, 100, 212]

    celsius_temps = [(f - 32) * 5/9 for f in fahrenheit_temps]

    print("Temperatures in Fahrenheit:")
    print(fahrenheit_temps)

    print("\nTemperatures in Celsius:")
    print(celsius_temps)

fahrenheit_to_celsius()
