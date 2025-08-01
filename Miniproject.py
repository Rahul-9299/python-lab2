# Student Report Card Management System
students = {}

# Add new student record
def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = list(map(float, input("Enter marks in subjects (space-separated): ").split()))
    students[roll] = {'name': name, 'marks': marks}
    print("Student record added.")

# View all student reports
def view_all():
    print("\nAll Student Reports:")
    for roll, info in students.items():
        print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")

# Display topper(s) based on average marks
def display_toppers():
    if not students:
        print("No records.")
        return
    max_avg = -1
    toppers = []
    for info in students.values():
        avg = sum(info['marks']) / len(info['marks'])
        if avg > max_avg:
            max_avg = avg
            toppers = [info['name']]
        elif avg == max_avg:
            toppers.append(info['name'])
    print(f"Topper(s) with average {max_avg}: {toppers}")

# Search for a student by roll number
def search_by_roll():
    roll = input("Enter roll number to search: ")
    if roll in students:
        info = students[roll]
        print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")
    else:
        print("Student not found.")

# Display all students who have failed in one or more subjects
def display_failed():
    fail_mark = float(input("Enter minimum passing mark: "))
    print("Students who failed in one or more subjects:")
    for roll, info in students.items():
        if any(m < fail_mark for m in info['marks']):
            print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")

# Update marks of any student
def update_marks():
    roll = input("Enter roll number to update marks: ")
    if roll in students:
        new_marks = list(map(float, input("Enter new marks (space-separated): ").split()))
        students[roll]['marks'] = new_marks
        print("Marks updated.")
    else:
        print("Student not found.")

while True:
    print("\nMenu:")
    print("1. Add new student record")
    print("2. View all student reports")
    print("3. Display topper(s)")
    print("4. Search by roll number")
    print("5. Display students who failed in one or more subjects")
    print("6. Update marks of a student")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_all()
    elif choice == '3':
        display_toppers()
    elif choice == '4':
        search_by_roll()
    elif choice == '5':
        display_failed()
    elif choice == '6':
        update_marks()
    elif choice == '7':
        break
    else:
        print("Invalid choice!")
