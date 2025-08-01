# Student Report Card Management System
students = {}
subject_names = input("Enter subject names (space-separated): ").split()
num_subjects = len(subject_names)

def add_multiple_students():
    count = int(input("How many students do you want to add? "))
    for _ in range(count):
        add_student()

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = []
    for subj in subject_names:
        mark = float(input(f"Enter marks for {subj}: "))
        marks.append(mark)
    students[roll] = {'name': name, 'marks': marks}
    print("Student record added.")

def view_all():
    print("\nAll Student Reports:")
    for roll, info in students.items():
        marks_str = ', '.join(f"{subj}: {mark}" for subj, mark in zip(subject_names, info['marks']))
        print(f"Roll: {roll}, Name: {info['name']}, Marks: [{marks_str}]")

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

def search_by_roll():
    roll = input("Enter roll number to search: ")
    if roll in students:
        info = students[roll]
        print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")
    else:
        print("Student not found.")

def display_failed():
    fail_mark = float(input("Enter minimum passing mark: "))
    print("Students who failed in one or more subjects is given below:")
    for roll, info in students.items():
        if any(m < fail_mark for m in info['marks']):
            print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}")
    else:
        print(f"hurray! no one is failed")

def update_marks():
    roll = input("Enter roll number to update marks: ")
    if roll in students:
        new_marks = []
        for subj in subject_names:
            mark = float(input(f"Enter new marks for {subj}: "))
            new_marks.append(mark)
        students[roll]['marks'] = new_marks
        print("Marks updated.")
    else:
        print("Student not found.")

while True:
    print("\nMenu:")
    print("1. Add new student record")
    print("2. Add multiple student records")
    print("3. View all student reports")
    print("4. Display topper(s)")
    print("5. Search by roll number")
    print("6. Display students who failed in one or more subjects")
    print("7. Update marks of a student")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        add_multiple_students()
    elif choice == '3':
        view_all()
    elif choice == '4':
        display_toppers()
    elif choice == '5':
        search_by_roll()
    elif choice == '6':
        display_failed()
    elif choice == '7':
        update_marks()
    elif choice == '8':
        break
    else:
        print("Invalid choice!")
