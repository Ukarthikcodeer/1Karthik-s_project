#STUDENT MANAGEMENT SYSTEM PROJECT BY KARTHIK

#importing json module
import json

PUPIL_INFO = "'karthik'_pupils.json"

# Creating a function to load
def load_students():
    try:
        with open(PUPIL_INFO, 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    return students

# Creating a function to save students
def save_students(students):
    with open(PUPIL_INFO, 'w') as file:
        json.dump(students, file, indent=4)

# creating a function called 'include_student' to include
def include_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = input("Enter student's grade: ")
    contact = input("Enter student's contact details: ")

    students = load_students()
    students.append({"name": name, "age": age, "grade": grade, "contact": contact})
    save_students(students)
    print("Student record added successfully!")

# Creating a function to show the students
def view_students():
    students = load_students()
    if students:
        print("\nStudent Records:")
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Contact: {student['contact']}")
    else:
        print("No student records found.")

# creating a function to search for a specific student by name or grade
def search_student():
    query = input("Enter the name of the student to search: ")

    students = load_students()
    found_students = []
    for student in students:
        if query.lower() in student['name'].lower() or query.lower() == student['grade'].lower():
            found_students.append(student)

    if found_students:
        print("\nFound Students:")
        for student in found_students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Contact: {student['contact']}")
    else:
        print("No matching student records found.")

# Function('update_student') to update a student's information
def update_student():
    query = input("Enter the name of the student to update: ")

    students = load_students()
    for student in students:
        if query.lower() in student['name'].lower():
            print(f"Student Found: Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}, Contact: {student['contact']}")
            new_age = int(input("Enter updated age: "))
            new_grade = input("Enter updated grade: ")
            new_contact = input("Enter updated contact details: ")
            student['age'] = new_age
            student['grade'] = new_grade
            student['contact'] = new_contact
            save_students(students)
            print("Student record updated successfully!")
            return
    print("No matching student found.")

# Function to delete a student info
def delete_student():
    query = input("Enter the name of the student to delete: ")

    students = load_students()
    updated_students = [student for student in students if query.lower() not in student['name'].lower()]

    if len(updated_students) < len(students):
        save_students(updated_students)
        print("Student record deleted successfully!")
    else:
        print("No matching student found.")

# Main function to perfome the code 
def main():
    while True:
        print("\nStudent Management System")
        print("1. Include Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            include_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()