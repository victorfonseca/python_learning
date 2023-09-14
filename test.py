import functools
import operator
import itertools
import bisect

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 4
print("The factorial of", num, "is", factorial(num))

lis = [1, 2, 3, 4, 5, 6]

print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, r: a+r, lis))

print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, r: a if a > r else r, lis))

print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))

print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))

print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))

print("The summation of list using accumulate is :", end="")
print(list(itertools.accumulate(lis, lambda x, y: x+y)))

print("The summation of list using reduce is :", end="")
print(functools.reduce(lambda x, y: x+y, lis))

numbers = (1, 2, 3, 4, 5)

result = map(lambda n : operator.mul(n, n), numbers)
print(list(result))

arr = sorted([2, 3, 4, 40, 3333, 300, 456, 1, 29, 100, 22, 10])
x = 10

i = bisect.bisect_left(arr, x)

if i != len(arr) and arr[i] == x:
    print(str(i))
else:
    print("Not found")