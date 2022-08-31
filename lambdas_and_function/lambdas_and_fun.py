def add(a: int, b: int) -> int:
    """ Add two numbers"""
    return a + b


print(add.__name__)


def operate(x, y, func):
    return func(x, y)


print(operate(2, 3, add))


def sub(x, y):
    return y - x


print(operate(5, 8, sub))

lst = [1, 2, 4, 5, 6]

from functools import reduce


def reduce_fun(acc, item):
    print(f"acc ->{acc} <> item -> {item}")
    return acc * item
    # return acc + item


from math import prod

print("\n################ Reduce ##############")
print(lst)
print(reduce(reduce_fun, lst, 100))
print(prod(lst, start=100))
# will do the same work that reduce does when multiplying
# print(reduce(lambda acc, item: acc if len(acc) > len(item) else item, fruits))
print(reduce(lambda acc, item: acc if acc > item else item, lst))
print(reduce(max, lst))
print(reduce(min, lst))

# def reduce_it(acc, item):
#     if acc > item:
#         acc
#     else:
#         item
#
#
# print(reduce_it(100, 2))

#               MATCH: VERY NEW TO PYTHON

print("############ match ############")
#
# num = int(input("Enter a number: "))
# match num:
#     case 1:
#         print(1)
#     case 2:
#         print(2)
#     case _:
#         print("Don't Know You")
#
#
# num = int(input("Enter a number: "))
# match num:
#     case _ as x if 1 <= x <= 10:
#         print(x)
#     case _ as x if 11 <= x <= 20:
#         print(x)
#     case 30 | 40| 50:
#         print(x)
#     case _:
#         print("Don't Know You")

lst = [20,13,16]
match lst:
    case [x,y,z]:
        print(x, y, z)
    case[a, [b, c], d]:
        print(a, b, c, d)
    case _:
        print("Nothing matched")


# d = {
#     "name": "Hadiza",
#     "age":18,
#     "is_swit": True
#     }
# match d

def fizzbuzz(num):
    three = num % 3
    five = num % 5

    match (three,five):
        case (0,0):
            print("FIZZBUZZ")
        case (0,_):
            print("FIZZ")
        case (_,0):
            print("BUZZ")
        case _:
            return num


for i in range(1, 101):
    print(fizzbuzz(i))


import itertools
# def suming_list(list_: list[int])))-> int | None