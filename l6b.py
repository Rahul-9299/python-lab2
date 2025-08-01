# Input n numbers and store them in a tuple
n = int(input("Enter the number of elements: "))
nums = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    nums.append(num)
nums_tuple = tuple(nums)

sorted_nums = sorted(nums_tuple)
if n % 2 == 1:
    median = sorted_nums[n // 2]
else:
    median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2

print(f"Tuple: {nums_tuple}")
print(f"Median (without built-in function): {median}")