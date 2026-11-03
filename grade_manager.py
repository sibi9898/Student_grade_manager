# ============================================================
# Student Grade Manager
# Week 1 - Day 2 Assignment
# ============================================================

# A list stores all students.
# Each student is a dictionary containing name, mark, and grade.
# A list allows two students to have the same name.
students = []


def get_grade(mark):
    """Return the grade for a mark using the assignment scale."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    """Ask for a student's details, validate them, and save them."""
    print("\n--- Add Student ---")

    # Get and validate the student's name.
    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty.")
        return

    # Get and validate the student's mark.
    mark_input = input("Enter marks (0-100): ").strip()

    try:
        mark = int(mark_input)
    except ValueError:
        print("Error: Please enter a whole number for marks.")
        return

    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100.")
        return

    # Calculate the grade and store the student.
    grade = get_grade(mark)

    student = {
        "name": name,
        "mark": mark,
        "grade": grade
    }

    students.append(student)
    print(f"Student '{name}' added successfully!")


def show_results():
    """Display all students and the class statistics."""
    print("\n--- Student Results ---")

    # Handle the case where no students have been added.
    if not students:
        print("No student records found. Please add a student first.")
        return

    # Print a neatly aligned results table.
    print("-" * 42)
    print(f"{'Name':<22}{'Mark':>8}{'Grade':>10}")
    print("-" * 42)

    for student in students:
        print(
            f"{student['name']:<22}"
            f"{student['mark']:>8}"
            f"{student['grade']:>10}"
        )

    print("-" * 42)

    # Calculate class statistics.
    marks = [student["mark"] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"Average: {average:.1f}")
    print(f"Highest: {highest}")
    print(f"Lowest:  {lowest}")


def main():
    """Display the menu and run the program until the user quits."""
    print("=" * 42)
    print("       STUDENT GRADE MANAGER")
    print("=" * 42)

    while True:
        print("\nMenu")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            show_results()

        elif choice == "3":
            print("\nThank you for using Student Grade Manager!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Start the program.
if __name__ == "__main__":
    main()