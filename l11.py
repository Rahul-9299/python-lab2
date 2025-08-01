# Input a list of numbers with duplicates
nums = list(map(float, input("Enter numbers separated by spaces: ").split()))
unique_nums = set(nums)
sorted_list = sorted(unique_nums)

print(f"Sorted list without duplicates: {sorted_list}")
