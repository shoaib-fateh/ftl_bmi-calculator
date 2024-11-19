from colorama import Fore, Style, init

init(autoreset=True)

# here bmi calculation will done
def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

# the main function
def main():

    print(Fore.CYAN + "\nWelcome to BMI Calculator!")

    # this will get the system (metric or imperial)
    system = input(Fore.YELLOW + "Choose Your System: metric (m) or imperial (i): ")

    # this if condition will check that which system it is
    if(system.lower() == "m"):
        weight = int(input(Fore.GREEN + "\nWrite Your Weight in kilogram: "))
        height = int(input(Fore.GREEN + "Write Your Height in centimeters: "))
    elif(system == "i"):
        weight = int(input(Fore.GREEN + "\nWrite Your Weight in pounds: ")) / 2.20462
        height = int(input(Fore.GREEN + "Write Your Height in inches: ")) / 39.3701
    else:
        print(Fore.WHITE + "\n(m) for metric, (i) for imperial")
        print(Fore.RED + "Invalid Input, Try again.\n")

        # re agin the function
        return main()
        
    # here it will do calculation and then store it in bmi varible
    bmi = round(calculate_bmi(weight, height), 2)

    # here it will check the bmi and print it out
    if(bmi < 18.5):
        print(Fore.BLUE + f"Underweight, your bmi is {bmi}")

    elif(bmi >= 18.5 and bmi <= 24.9):
        print(Fore.GREEN + f"Normal weight, your bmi is {bmi}")

    elif(bmi >= 25 and bmi <= 29.9):
        print(Fore.YELLOW + f"Overweight, your bmi is {bmi}")

    elif(bmi >= 30):
        print(Fore.RED + f"Obesity, your bmi is {bmi}")
        
    # final message
    print(Style.BRIGHT + Fore.CYAN + "\nThank you for using the BMI calculator!")
    

# running the main loop to begin the mini app
main()


