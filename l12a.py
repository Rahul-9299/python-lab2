# Create a dictionary for student names and their scores in three subjects
students = {}
n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("Enter student name: ")
    scores = list(map(float, input("Enter scores in 3 subjects (space-separated): ").split()))
    students[name] = scores

def display_averages(students):
    print("\nAverage marks of each student:")
    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        print(f"{name}: {avg}")

display_averages(students)
