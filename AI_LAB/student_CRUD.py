# Initialize an empty list of students
students = []

while True:
    # Display the menu
    print("\nMenu:")
    print("1. Add a student")
    print("2. Remove a student")
    print("3. Edit a student's name")
    print("4. Display students")
    print("5. Exit")

    # Take the user's choice
    choice = int(input("\nEnter your choice (1-5): "))

    # Option 1: Add a student
    if choice == 1:
        name = input("Enter the name of the student to add: ")
        students.append(name)
        print(f"Student '{name}' added to the list.")

    # Option 2: Remove a student
    elif choice == 2:
        name = input("Enter the name of the student to remove: ")
        if name in students:
            students.remove(name)
            print(f"Student '{name}' removed from the list.")
        else:
            print(f"Student '{name}' not found in the list.")

    # Option 3: Edit a student's name
    elif choice == 3:
        try:
            position = int(input("Enter the student's position number to edit (1-based index): ")) - 1
            if 0 <= position < len(students):
                new_name = input(f"Enter the new name for student {students[position]}: ")
                students[position] = new_name
                print(f"Student's name updated to '{new_name}'.")
            else:
                print("Invalid position number.")
        except ValueError:
            print("Please enter a valid number.")

    # Option 4: Display the list of students
    elif choice == 4:
        if students:
            print("\nCurrent List of Students:")
            for i, student in enumerate(students):
                print(f"{i + 1}. {student}")
        else:
            print("No students in the list.")

    # Option 5: Exit
    elif choice == 5:
        print("Exiting the program.")
        break

    # If user enters an invalid choice
    else:
        print("Invalid choice, please enter a number between 1 and 5.")
