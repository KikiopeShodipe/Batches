def divide_numbers():
try:
num1 = input("Enter the 1st Number: ")
num2 = input("Enter the 2nd Number: ")
# Check for non-integer input
if not num1.lstrip('-').isdigit() or not num2.lstrip('-').isdigit():
raise ValueError("Inputs must be valid integers.")
# Convert to integers
num1 = int(num1)
num2 = int(num2)
# Raise error if numbers are negative (as a demonstration)
if num1 < 0 or num2 < 0:
raise Exception("Negative numbers are not allowed.")
# Raise division by zero
if num2 == 0:
raise ZeroDivisionError("You cannot divide by zero.")
# Simulate TypeError (just to show how it can be raised)
if isinstance(num1, int) and isinstance(num2, int):
result = num1 / num2
print(f"✅ The result is: {result}")
else:
raise TypeError("Operands must be integers.")
except ValueError as ve:
print(f"❌ ValueError: {ve}")
except ZeroDivisionError as zde:
print(f"❌ ZeroDivisionError: {zde}")
except TypeError as te:
print(f"❌ TypeError: {te}")
except Exception as e:
print(f"❌ General Exception: {e}"
finally:
print("🔁 This block always runs.")
# Run the function
divide_numbers()