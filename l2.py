# Input first list
n1 = int(input("Enter the number of elements in the first list: "))
list1 = []
for i in range(n1):
    num = int(input(f"Enter element {i+1} for first list: "))
    list1.append(num)

# Input second list
n2 = int(input("Enter the number of elements in the second list: "))
list2 = []
for i in range(n2):
    num = int(input(f"Enter element {i+1} for second list: "))
    list2.append(num)

# Merge the two lists
merged_list = list1 + list2

# Find common elements
common_elements = set(list1) & set(list2)

# Remove common elements from merged list
result_list=list(set(merged_list)-common_elements)

print(f"Merged list after removing common elements: {result_list}")
