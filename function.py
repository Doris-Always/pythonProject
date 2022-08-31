# def add(first_number: int, second_number: int) -> int:
#     """
#     :param first_number:
#     :param second_number:
#     :return: int
#     """
#     return first_number + second_number
#
#
# print(add(3, 6))
# # print(help(add)) or
# print(add.__doc__)
# print(add.__name__)
# print(add.__annotations__)


# def celsius_to_fah(celsius_float):
#     return celsius_float * 1.8 + 32
import math
def get_digit(number, position):
    """return digit at position in number
    counting from right"""
    return number // (10 ** position) % 10


print(get_digit(3794, 2))


# def get_length(number):

    # return math.ceil(math.log10(number))


#     for index in range(number):
#         return index + 1
#
#
# print(get_length(5289))

# number: int = int(input("enter a number"))
# number = number**2
# num = str(number)
#
# for i in num:
#     print(i, end='')
#     if i in num == number:
