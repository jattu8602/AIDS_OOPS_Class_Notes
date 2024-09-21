# Simple True/False evaluator
while True:
    # Get user input
    statement = input("\nEnter a statement (or type 'exit' to quit): ")

    # Allow the user to exit the loop
    if statement.lower() == "exit":
        print("Exiting the program.")
        break

    try:
        # Evaluate the statement and print whether it's True or False
        result = eval(statement)
        if isinstance(result, bool):  # Check if the result is a boolean
            print(f"The statement is {result}.")
        else:
            print(f"The statement '{statement}' does not evaluate to a boolean.")
    except Exception as e:
        print(f"Error evaluating the statement: {e}")
