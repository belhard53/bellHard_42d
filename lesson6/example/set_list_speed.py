# import time
# print(time.time())

from time import time
print(time())




# start = time()

# a = 10000**1000000

# end = time()
# print(end - start)

from timeit import timeit

a = list(range(100000))
b = set(a)
c = tuple(a)

print(timeit("111 in a", globals={"a":a}))
print(timeit("111 in a", globals={"a":b}))
print(timeit("111 in a", globals={"a":c}))

print(a.__sizeof__())
print(b.__sizeof__())
print(c.__sizeof__())

