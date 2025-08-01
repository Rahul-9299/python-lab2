# Create a dictionary for student names and their scores in three subjects
students = {}
n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("Enter student name: ")
    scores = list(map(float, input("Enter scores in 3 subjects (space-separated): ").split()))
    students[name] = scores

def find_topper(students):
    topper = None
    top_avg = -1
    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        if avg > top_avg:
            top_avg = avg
            topper = name
    print(f"Topper: {topper} with average marks {top_avg}")

find_topper(students)