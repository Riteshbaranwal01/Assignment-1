# Code for a Calculator.
print("Calculator")

# Take inputs.
a = float(input("Enter 1st number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter 2nd number: "))

# Perform operation
if op == "+":
    print("Sum =", a + b)
elif op == "-":
    print("Subtract =", a - b)
elif op == "*":
    print("Multiply =", a * b)
elif op == "/":
    if b != 0:
       print("Division =", a / b)
    else:
       print("Not possible.")
elif op == "+, -, *, /":
      print("All result =", a + b, a - b, a * b, a / b)
else:
    print("Invalid operator")

# Thank you 😊 
