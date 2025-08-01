# Input n numbers and store them in a list
n = int(input("Enter the number of elements: "))
nums = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)

# a) Using built-in functions
max_builtin = max(nums)
min_builtin = min(nums)
print(f"Using built-in functions: Max = {max_builtin}, Min = {min_builtin}")

# b) Without using built-in functions
max_manual = nums[0]
min_manual = nums[0]
for num in nums[1:]:
    if num > max_manual:
        max_manual = num
    if num < min_manual:
        min_manual = num
print(f"Without using built-in functions: Max = {max_manual}, Min = {min_manual}")
