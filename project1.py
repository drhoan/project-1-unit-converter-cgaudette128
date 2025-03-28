Choose_conversion = input("Choose conversion (1 for Fahrenheit to Celsius, 2 for Celcius to Fahrenheit, 3 for miligrams to Tons, 4 for Tons to Miligrams, 5 for Feet to Meters, 6 for Meters to Feet, 0 to Quit): ")

while True: 
    Choose_conversion = input("Choose conversion (1 for Fahrenheit to Celsius, 2 for Celcius to Fahrenheit, 3 for miligrams to Tons, 4 for Tons to Miligrams, 5 for Feet to Meters, 6 for Meters to Feet, 0 to Quit): ")
    
    if Choose_conversion == '1':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5.0/9.0
        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")

    elif Choose_conversion == '2':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9.0/5.0) + 32
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")

    elif Choose_conversion == '3':
        milligrams = float(input("Enter weight in milligrams: "))
        tons = milligrams / 1e9
        print(f"{milligrams} milligrams is equal to {tons} tons")

    elif Choose_conversion == '4':
        tons = float(input("Enter weight in tons: "))
        milligrams = tons * 1e9
        print(f"{tons} tons is equal to {milligrams} milligrams")

    elif Choose_conversion == '5':
        feet = float(input("Enter length in feet: "))
        meters = feet / 3.28084
        print(f"{feet} feet is equal to {meters} meters")

    elif Choose_conversion == '6':
        meters = float(input("Enter length in meters: "))
        feet = meters * 3.28084
        print(f"{meters} meters is equal to {feet} feet")

    elif Choose_conversion == '0':
        print("Bye try again another time.")
        break

    else:
        print("Invalid choice. Please select a valid conversion option.") 






