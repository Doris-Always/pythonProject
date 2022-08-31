def list_sum(arr: list, target: int) -> list:
    index1 = 0
    index2 = 0

    length_of_list = len(arr)
    for index1 in range(length_of_list - 1):
        for index2 in range(index1 + 1, length_of_list):
            if arr[index1] + arr[index2] == target:
                return [index1, index2]


print(list_sum([3, -1, 5, 4], 3))


# to check if brackets in a list are a balanced pair
def balance_pair(bracket: str) -> bool:
    if not bracket or len(bracket) % 2 == 1:
        return False
    stack: list = []
    for bracket in bracket:
        if bracket in "{[(":
            stack.append(bracket)
        elif bracket in "}])":
            peek: str = stack[-1]
            if peek == "{" and bracket == "}":
                stack.pop()
            elif peek == "[" and bracket == "]":
                stack.pop()
            elif peek == "(" and bracket == ")":
                stack.pop()
        else:

            return False
    return True


print(balance_pair("[]"))

derrick = {'name': 'Derek', 'age': 18, 'status': 'Married'}

for key, value in derrick.items():
    print(f"{key}-->{value}")


def string_dic(iterable: list | str | tuple) -> dict:
    my_dict = {}

    for item in iterable:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1

    return my_dict


print(string_dic("hello"))


def number_dict(iterable: list | str | tuple) -> dict:
    my_number = {}

    for i in iterable:
        if i in my_number:
            my_number[i] += 1
        else:
            my_number[i] = 1

    return my_number


print(number_dict({1, 2, 4, 3, 5, 3, 2, 1}))


#  OR
def string_dic(iterable: list | str | tuple) -> dict:
    my_dict = {}
    for i in iterable:
        # my_dict[i] = iterable.count(i)
        my_dict[i] = my_dict.get(i, 0) + 1

    return my_dict


print(string_dic("helllo"))


# OR
def string_dic(iterable: list | str | tuple) -> dict:
    from collections import Counter, defaultdict

    my_dict = defaultdict(int)
    for i in iterable:

        my_dict[i] += 1
