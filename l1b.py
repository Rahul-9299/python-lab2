# Input n numbers and store them in a list
n = int(input("Enter the number of elements: "))
nums = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    nums.append(num)

# a) Using built-in functions
sorted_builtin = sorted(nums)
print(f"Sorted list using built-in function: {sorted_builtin}")

# b) Without using built-in functions (using bubble sort)
sorted_manual = nums.copy()
for i in range(len(sorted_manual)):
    for j in range(0, len(sorted_manual) - i - 1):
        if sorted_manual[j] > sorted_manual[j + 1]:
            sorted_manual[j], sorted_manual[j + 1] = sorted_manual[j + 1], sorted_manual[j]
print(f"Sorted list without using built-in function: {sorted_manual}")
