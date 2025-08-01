
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def even_index_and_primes(lst):
    result = []
    for i, val in enumerate(lst):
        if i % 2 == 0 or is_prime(val):
            result.append(val)
    return result

# Accept list from user
user_input = input("Enter numbers separated by spaces: ")
data = list(map(int, user_input.split()))
filtered = even_index_and_primes(data)
print(f"Original list: {data}")
print(f"Filtered list (even indexes or primes): {filtered}")