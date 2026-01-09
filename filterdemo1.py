#filter example

l1 = [2,5,10,23,45,6,8,10,9,100]

# filter(function,iterable)

k=filter(lambda x: x % 2 == 0, l1)

print(list(k))

