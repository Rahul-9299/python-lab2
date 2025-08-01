# Input n numbers and store them in a tuple
n = int(input("Enter the number of elements: "))
nums = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    nums.append(num)
nums_tuple = tuple(nums)

# Calculate average
total = 0
for num in nums_tuple:
    total += num
average = total / n if n > 0 else 0

print(f"Tuple: {nums_tuple}")
print(f"Average: {average}")
