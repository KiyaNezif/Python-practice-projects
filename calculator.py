# Python calculator 
#where a user can input two numbers and an operator, and the program will perform the calculation and display the result.
# Function to perform the calculation


operator = input("Enter an operator (+, -, *, /): ")
# use float to convert the input to a number

num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))

if operator == '+':
 result = num1 + num2
elif operator == '-':
 result = num1 - num2
elif operator == '*':
 result = num1 * num2
elif operator == '/':
 result = num1 / num2

print("Result:", result)
