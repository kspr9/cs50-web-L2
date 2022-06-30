import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input. Expected type int.")
    sys.exit()
try:
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by 0.")
    sys.exit(1)


print(f"{x} / {y} = {result}")
