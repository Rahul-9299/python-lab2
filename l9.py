import random

# Create a set of random numbers until it has 10 unique elements
num_set = set()
while len(num_set) < 10:
    num_set.add(random.randint(1, 100))

print(f"Original set: {num_set}")
smallest = min(num_set)
largest = max(num_set)
num_set.remove(smallest)
num_set.remove(largest)

print(f"Set after removing smallest ({smallest}) and largest ({largest}): {num_set}")
