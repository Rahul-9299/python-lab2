# Input master list of all students
master = set(input("Enter roll numbers of all students (space-separated): ").split())
cricket = set(input("Enter roll numbers of students who play cricket (space-separated): ").split())
football = set(input("Enter roll numbers of students who play football (space-separated): ").split())
neither = master - (cricket | football)

print(f"Students who play neither cricket nor football: {sorted(neither)}")

both = cricket & football

print(f"Students who play both cricket and football: {sorted(both)}")

only_one = cricket ^ football

print(f"Students who play only one sport: {sorted(only_one)}")
