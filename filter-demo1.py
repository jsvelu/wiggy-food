# Example: Filter out only even numbers
numbers = [1, 2, 3, 4, 5, 6]

#var = list(filter(function, iterable)
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)  # [2, 4, 6]
