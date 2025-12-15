def TemperatureChecker():
    temp = float(input("Enter the temperature in Celsius: "))
    if temp >= 30:
        print("It's a hot day.")
    elif 20 <= temp <= 30:
        print("It's a warm day.")
    else:
        print("It's a cold day.")
TemperatureChecker()
