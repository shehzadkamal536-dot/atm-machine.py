
students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add New Student
    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        student_class = input("Enter class: ")
        marks = input("Enter marks: ")

        student = {
            "name": name,
            "roll": roll,
            "class": student_class,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    # View All Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found!")

        else:
            print("\n===== ALL STUDENTS =====")

            for student in students:
                print("Name:", student["name"])
                print("Roll Number:", student["roll"])
                print("Class:", student["class"])
                print("Marks:", student["marks"])
                print("----------------------")

    # Search Student
    elif choice == "3":
        search_roll = input("Enter roll number to search: ")
        found = False

        for student in students:
            if student["roll"] == search_roll:
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Roll Number:", student["roll"])
                print("Class:", student["class"])
                print("Marks:", student["marks"])
                found = True
                break

        if found == False:
            print("Student not found!")

    # Delete Student
    elif choice == "4":
        delete_roll = input("Enter roll number to delete: ")
        found = False

        for student in students:
            if student["roll"] == delete_roll:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if found == False:
            print("Student not found!")

    # Exit
    elif choice == "5":
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid choice! Please try again.")
