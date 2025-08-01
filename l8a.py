# Input roll numbers of students who play cricket
cricket = set(input("Enter roll numbers of students who play cricket (space-separated): ").split())
football = set(input("Enter roll numbers of students who play football (space-separated): ").split())
both = cricket & football

print(f"Students who play both cricket and football: {sorted(both)}")