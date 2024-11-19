

weight = int(input("Your Weight: "))
height = int(input("Your Height: "))

def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)


print(calculate_bmi(weight, height))


