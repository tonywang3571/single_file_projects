# Simple calculator

# user input num1
num1 = float(input("Enter a number: "))

# user input oper
oper = input("Enter an operator (+, -, *, /): ")

# user input num2
num2 = float(input("Enter another number: "))

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
    print(num1 * num2)
elif oper == "/" and num2 != 0:
    print(num1 / num2)
elif oper == "/" and num2 == 0:
    print("Invalid, can't divide by zero.")
else:
    print("Invalid entry.")

