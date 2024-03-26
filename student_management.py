students = {}

def add_student():
    student_id = input("Enter student ID:- ")
    if student_id in students:
        print("Student ID already exists. Please allot different ID.")
        return
    name = input("Enter student name:- ")
    age = input("Enter student age:- ")
    grade = input("Enter student grade:- ")
    students[student_id] = {'name': name, 'age': age, 'grade': grade}
    print("Student added successfully.")

def remove_student():
    student_id = input("Enter student ID to remove: ")
    if student_id in students:
        del students[student_id]
        print("Student with Student ID = ",student_id,"removed successfully.")
    else:
        print("No student exist with Student ID = ",student_id,".")

def update_student_details():
    student_id = input("Enter student ID to update details:- ")
    if student_id in students:
        name = input("Enter new name :- ")
        age = input("Enter new age :- ")
        grade = input("Enter new grade :- ")
        if name:
            students[student_id]['name'] = name
        if age:
            students[student_id]['age'] = age
        if grade:
            students[student_id]['grade'] = grade
        print("Student information updated successfully.")
    else:
        print("No student exist with Student ID = ",student_id,".")

def search_student():
    query = input("Enter student name or ID to search: ")
    found = False
    for student_id, info in students.items():
        if query == student_id or query.lower() in info['name'].lower():
            #print(f"Student ID -> {student_id}, Name -> {info['name']}\n, Age -> {info['age']}, Grade -> {info['grade']}")
            print("Student ID ->",student_id)
            print("Name ->",info['name'])
            print("Age ->",info['age'])
            print("Grade ->",info['grade'])
            
            found = True
    if not found:
        print("Student not found.")

def display_all_students():
    print("All Students:")
    for student_id, info in students.items():
        print(f"Student ID: {student_id}, Name: {info['name']}, Age: {info['age']}, Grade: {info['grade']}")

def main():
    while True:
        print("\nGLA Student Management System ")
        print("1 :- Add a student")
        print("2 :- Remove a student")
        print("3 :- Update student information")
        print("4 :- Search for a student")
        print("5 :- Display all students")
        print("6 :- Exit")
        
        choice = input("Enter your choice:- ")

        if choice == '1':
            add_student()
        elif choice == '2':
            remove_student()
        elif choice == '3':
            update_student_details()
        elif choice == '4':
            search_student()
        elif choice == '5':
            display_all_students()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
