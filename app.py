# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    return x / y

# Take two inputs from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Print the menu
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get the user's choice
choice = input("Enter your choice (1-4): ")

# Perform the selected operation
if choice == '1':
    result = add(num1, num2)
    operation = "Addition"
elif choice == '2':
    result = subtract(num1, num2)
    operation = "Subtraction"
elif choice == '3':
    result = multiply(num1, num2)
    operation = "Multiplication"
elif choice == '4':
    result = divide(num1, num2)
    operation = "Division"
else:
    print("Invalid choice")
    exit()

# Print the result
print(f"{operation} result: {result}")
