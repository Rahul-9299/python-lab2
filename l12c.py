# Create a dictionary for student names and their scores in three subjects
students = {}
n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("Enter student name: ")
    scores = list(map(float, input("Enter scores in 3 subjects (space-separated): ").split()))
    students[name] = scores

def update_marks(students):
    name = input("Enter the student name to update marks: ")
    if name in students:
        new_scores = list(map(float, input("Enter new scores in 3 subjects (space-separated): ").split()))
        students[name] = new_scores
        print(f"Updated marks for {name}.")
    else:
        print("Student not found.")

update_marks(students)
print("\nUpdated student records:")
for name, scores in students.items():
    print(f"{name}: {scores}")
