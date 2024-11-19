

# here bmi calculation will done
def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)


# the main function
def main():

    # this will get the system (metric or imperial)
    system = input("Your System: metric (m) or imperial (i): ")

    # this if condition will check that which system it is
    if(system == "m"):
        weight = int(input("Your Weight in kilogram: "))
        height = int(input("Your Height in centimeters: "))
    elif(system == "i"):
        weight = int(input("Your Weight in pounds: ")) / 2.20462
        height = int(input("Your Height in inches: ")) / 39.3701
    else:
        print("Try again.")

        # re agin the function
        return main()
        

    # here it will do calculation and then store it in bmi varible
    bmi = calculate_bmi(weight, height)

    # here it will check the bmi and print it out
    if(bmi < 18.5):
        print(f"Underweight, your bmi is {bmi}")

    elif(bmi >= 18.5 and bmi <= 24.9):
        print(f"Normal weight, your bmi is {bmi}")

    elif(bmi >= 25 and bmi <= 29.9):
        print(f"Overweight, your bmi is {bmi}")

    elif(bmi >= 30):
        print(f"Obesity, your bmi is {bmi}")
    


# running the main loop to begin the mini app
main()


