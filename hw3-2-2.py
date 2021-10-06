# Author: CRS 9/29/21
weight = int(input("Please enter your weight."))
height = int(input("Please enter your height."))
bmi = weight / (height ** 2)
if bmi < 19:
    print("Underweight.")
elif bmi < 25:
    print("Healthy.")
elif bmi < 30:
    print("Overweight.")
elif bmi < 40:
    print("Obese.")
elif bmi >= 40:
    print("Extremely obese.")
