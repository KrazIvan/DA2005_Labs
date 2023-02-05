# Lab 1. Temperature conversion. DA2005 Programming techniques HT22. Stockholm University. Ivan Shabalin.

# Functions for converting across different temperature scales.
def celsius_to_fahrenheit(answer):
    t_fahrenheit = ((answer * 9/5) + 32)
    return t_fahrenheit

def celsius_to_kelvin(answer):
    t_kelvin = (answer + 273.15)
    return t_kelvin

def fahrenheit_to_celsius(answer):
    t_celsius = ((answer - 32) * 5/9)
    return t_celsius

def fahrenheit_to_kelvin(answer):
    t_kelvin = ((answer - 32) * 5/9 + 273.15)
    return t_kelvin

def kelvin_to_celsius(answer):
    t_celsius = (answer - 273.15)
    return t_celsius

def kelvin_to_fahrenheit(answer):
    t_fahrenheit = ((answer - 273.15) * 9/5 + 32)
    return t_fahrenheit


def main(conversion): # Main function of the program. 
    match conversion:
        case "1":
            answer = input("You selected Celsius to Fahrenheit.\nEnter a temperature in Celsius to convert to Fahrenheit: ").replace(" ", "")
            quitChecker(answer)
            while not floatChecker(answer):
                answer = input("Invalid input. Try again.\n\nEnter a temperature in Celsius to convert to Fahrenheit: ").replace(" ", "")
                quitChecker(answer)
            answer = float(answer)
            print(f"\n\nFahrenheit: {round(celsius_to_fahrenheit(answer), 5)}")
            restart()

        case "2":
            answer = input("You selected Celsius to Kelvin.\nEnter a temperature in Celsius to convert to kelvins: ").replace(" ", "")
            quitChecker(answer)
            while not floatChecker(answer):
                answer = input("Invalid input. Try again.\n\nEnter a temperature in Celsius to convert to kelvins: ").replace(" ", "")
                quitChecker(answer)
            answer = float(answer)
            print(f"\n\nKelvin: {round(celsius_to_kelvin(answer), 5)}")
            restart()

        case "3":
            answer = input("You selected Fahrenheit to Celsius.\nEnter a temperature in Fahrenheit to convert to Celsius: ").replace(" ", "")
            quitChecker(answer)
            while not floatChecker(answer):
                answer = input("Invalid input. Try again.\n\nEnter a temperature in Fahrenheit to convert to Celsius: ").replace(" ", "")
                quitChecker(answer)
            answer = float(answer)
            print(f"\n\nCelsius: {round(fahrenheit_to_celsius(answer), 5)}")
            restart()

        case "4":
            answer = input("You selected Fahrenheit to Kelvin.\nEnter a temperature in Fahrenheit to convert to kelvins: ").replace(" ", "")
            quitChecker(answer)
            while not floatChecker(answer):
                answer = input("Invalid input. Try again.\n\nEnter a temperature in Fahrenheit to convert to kelvins: ").replace(" ", "")
                quitChecker(answer)
            answer = float(answer)
            print(f"\n\nKelvin: {round(fahrenheit_to_kelvin(answer), 5)}")
            restart()

        case "5":
            answer = input("You selected Kelvin to Celsius.\nEnter a temperature in Kelvin to convert to Celsius: ").replace(" ", "")
            quitChecker(answer)
            while not floatChecker(answer):
                answer = input("Invalid input. Try again.\n\nEnter a temperature in Kelvin to convert to Celsius: ").replace(" ", "")
                quitChecker(answer)
            answer = float(answer)
            print(f"\n\nCelsius: {round(kelvin_to_celsius(answer), 5)}")
            restart()

        case "6":
            answer = input("You selected Kelvin to Fahrenheit.\nEnter a temperature in Kelvin to convert to Fahrenheit: ").replace(" ", "")
            quitChecker(answer)
            while not floatChecker(answer):
                answer = input("Invalid input. Try again.\n\nEnter a temperature in Kelvin to convert to Fahrenheit: ").replace(" ", "")
                quitChecker(answer)
            answer = float(answer)
            print(f"\n\nFahrenheit: {round(kelvin_to_fahrenheit(answer), 5)}")
            restart()

        case "q":
            quit()

def restart(): # Asks the user if he wants to convert again or quit.
    restart = input("\nWant to convert something else? Input \"y\" or \"yes\" to convert again, or \"q\" to quit.\n\n").replace(" ", "").replace(".", "").upper()
    while not (restart == "Y") and (restart != "YES") and not (restart == "Q"):
        restart = input("\nI don't understand. Input \"y\" or \"yes\" to convert again, or \"q\" to quit.\n\n").replace(" ", "").replace(".", "").upper()
    if restart == "Y" or restart == "YES":
        newConversion()
    if restart == "Q":
        quit()

def newConversion(): # Asks the user for another conversion.
    conversion = input("\n\nWhat do you want to convert now?\n\n1. Celsius to Fahrenheit.\n2. Celsius to Kelvin.\n3. Fahrenheit to Celsius.\n4. Fahrenheit to Kelvin.\n5. Kelvin to Celsius.\n6. Kelvin to Fahrenheit.\n\n").replace(" ", "").replace(".", "").lower()
    while not (conversion == "1") and (conversion != "2") and not (conversion == "3") and (conversion != "4") and not (conversion == "5") and (conversion != "6") and not (conversion == "q"):
        conversion = input("Invalid request.\nInput \"1\", \"2\", \"3\", \"4\", \"5\", \"6\" to select, or \"q\" to quit. Nothing else.\n\nWhat kind of conversion do you want?\n1. Celsius to Fahrenheit.\n2. Celsius to Kelvin.\n3. Fahrenheit to Celsius.\n4. Fahrenheit to Kelvin.\n5. Kelvin to Celsius.\n6. Kelvin to Fahrenheit.\n\n").replace(" ", "").replace(".", "").lower()
    if conversion == "q":
        quit()
    else:
        main(conversion)

def quitChecker(answer): # Quits the program if the user inputs to quit the program during the temperature input prompt.
    if answer == "q" or answer == "Q":
        quit()
    else:
        pass

def floatChecker(answer): # Returns true if "answer" can be converted to a float without causing a ValueError. This is to avoid a ValueError crash if the user inputs something that can't be converted to a float, and to only convert things that won't cause a ValueError.
    try:
        float(answer)
        return True
    except ValueError:
        return False

# Introduction
conversion = input("\n\nHello. Welcome to Ivan's Temperature Converter.\n\nWhat kind of conversion do you want?\n1. Celsius to Fahrenheit.\n2. Celsius to Kelvin.\n3. Fahrenheit to Celsius.\n4. Fahrenheit to Kelvin.\n5. Kelvin to Celsius.\n6. Kelvin to Fahrenheit.\n\n").replace(" ", "").replace(".","").lower()
while not (conversion == "1") and (conversion != "2") and not (conversion == "3") and (conversion != "4") and not (conversion == "5") and (conversion != "6") and not (conversion == "q"):
    conversion = input("Invalid request.\nInput \"1\", \"2\", \"3\", \"4\", \"5\", \"6\" to select, or \"q\" to quit. Nothing else.\n\nWhat kind of conversion do you want?\n1. Celsius to Fahrenheit.\n2. Celsius to Kelvin.\n3. Fahrenheit to Celsius.\n4. Fahrenheit to Kelvin.\n5. Kelvin to Celsius.\n6. Kelvin to Fahrenheit.\n\n").replace(" ", "").replace(".","").lower()
main(conversion)