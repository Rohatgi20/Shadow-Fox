# Ask the user to input their height in meters
height = float(input("Enter height in meters: "))

# Ask the user to input their weight in kilograms
weight = float(input("Enter weight in kilograms: "))

# Calculate BMI using the formula: BMI = weight / (height^2)
bmi = weight / (height ** 2)

# Determine the BMI category and print the result
if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")
