
def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)

def main():
    weight = int(input("Your Weight: "))
    height = int(input("Your Height: "))

    bmi = calculate_bmi(weight, height)

    if(bmi < 18.5):
        print(f"Underweight, your bmi is {bmi}")

    elif(bmi >= 18.5 and bmi <= 24.9):
        print(f"Normal weight, your bmi is {bmi}")

    elif(bmi >= 25 and bmi <= 29.9):
        print(f"Overweight, your bmi is {bmi}")

    elif(bmi >= 30):
        print(f"Obesity, your bmi is {bmi}")
    
main()


