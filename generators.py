print("Generate")

# iterator and iterable
list1 = [2, 3, 4]
# for i in list1:
#     print(i)

# # iterator convert
# i = iter(list1)
# print(next(i))
# print(next(i))
# print(next(i))

# Generator create kora
def num_gen(n):
    for i in range(1, n+1):
        yield i



numbers = num_gen(11)
for i in numbers:
    print(i)

for i in numbers:
    print(i)