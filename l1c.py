# Input n numbers and store them in a list
n = int(input("Enter the number of elements: "))
nums = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    nums.append(num)

# a) Using built-in functions (set)
no_duplicates_builtin = list(set(nums))
print(f"List after removing duplicates using built-in function: {no_duplicates_builtin}")

# b) Without using built-in functions
no_duplicates_manual = []
for num in nums:
    if num not in no_duplicates_manual:
        no_duplicates_manual.append(num)
print(f"List after removing duplicates without using built-in function: {no_duplicates_manual}")
