import math


def anagram(number):
    my_square = number * number
    length_of_number = math.ceil(math.log10(number))
    if my_square % 10 ** length_of_number == number:
        print(number, "is an anagram")
    else:
        print(number, "is not an anagram")


anagram(25)
