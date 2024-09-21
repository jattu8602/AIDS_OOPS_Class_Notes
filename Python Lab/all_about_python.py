
# All About Python: An Introduction for Beginners
# ---------------------------------------------------
# Python is a high-level, interpreted, and general-purpose programming language.
# It is known for its simplicity, readability, and wide range of applications, from web development to data science and artificial intelligence.

# History of Python:
# - Python was created by Guido van Rossum and was first released in 1991.
# - It was designed to be simple and easy to understand, with an emphasis on code readability.
# - Python's popularity has grown steadily due to its clean syntax, large standard library, and strong community support.

# Key Features of Python:
# - **Easy to Learn and Use**: Python's simple syntax makes it easy for beginners to learn and start coding.
# - **Interpreted Language**: Python code is executed line by line, which makes debugging easier.
# - **Cross-Platform**: Python is available on multiple platforms, including Windows, macOS, and Linux.
# - **Large Standard Library**: Python comes with a vast collection of modules and libraries that support everything from regular expressions to networking.
# - **Dynamic Typing**: You don’t need to declare variable types explicitly. Python infers the type based on the value you assign.
# - **Multi-Paradigm**: Python supports procedural, object-oriented, and functional programming paradigms.

# Sample Code: Simple Python Program (Calculator)

# This is a basic calculator program that takes user input and performs basic arithmetic operations.

# Define a function for addition
def add(x, y):
    return x + y

# Define a function for subtraction
def subtract(x, y):
    return x - y

# Define a function for multiplication
def multiply(x, y):
    return x * y

# Define a function for division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Main function to run the calculator
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        # Check if choice is one of the options
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            # Ask if the user wants another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input")

# Run the calculator
if __name__ == "__main__":
    calculator()

# ---------------------------------------------------
# Conclusion:
# Python is one of the most popular and versatile programming languages.
# Its simplicity, combined with powerful capabilities, makes it an ideal choice for beginners and experienced developers alike.
# Whether you're building web applications, automating tasks, analyzing data, or experimenting with machine learning, Python has the tools you need.
