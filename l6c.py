# Input n numbers and store them in a tuple
n = int(input("Enter the number of elements: "))
nums = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    nums.append(num)
nums_tuple = tuple(nums)

max_count = 0
mode = None
for i in range(n):
    count = 0
    for j in range(n):
        if nums_tuple[j] == nums_tuple[i]:
            count += 1
    if count > max_count:
        max_count = count
        mode = nums_tuple[i]

print(f"Tuple: {nums_tuple}")
if max_count > 1:
    print(f"Mode (without built-in functions): {mode}")
else:
    print("No mode (all values are unique)")
