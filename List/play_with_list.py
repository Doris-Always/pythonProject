list_of_numbers = []
# add items in the list using for loops
for i in range(1, 10):
    list_of_numbers += [i]

print(list_of_numbers)

for item in list_of_numbers:
    print(item)

print("Index Value")
for i in range(len(list_of_numbers)):
    print("%4d %4d " % (i, list_of_numbers[i]))
print("modified list")
list_of_numbers[4] = 20
print(list_of_numbers)
