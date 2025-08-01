# Input roll numbers of students who play cricket
cricket = set(input("Enter roll numbers of students who play cricket (space-separated): ").split())
football = set(input("Enter roll numbers of students who play football (space-separated): ").split())
only_one = cricket ^ football

print(f"Students who play only one sport: {sorted(only_one)}")
