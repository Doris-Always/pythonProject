cont = []

for i in range(1, 11):
    cont.append(i)

print(cont)

# using collections
cont = [i for i in range(1, 11)]
print(cont)

squares = [num ** 2 for num in range(1, 11)]
print(squares)

names = ['bimpe', 'Banke', 'abimbola', 'James', 'Racheal']
my_names = []
for name in names:
    if name.istitle():
        my_names.append(name)

print(my_names)

names = ['bimpe', 'Banke', 'abimbola', 'James', 'Racheal']
my_names = [name for name in names if name.istitle()]
print(my_names)

evens = [even for even in range(1, 11) if even % 2 == 0]
print(evens)

even_squared_odd_cubed = [num ** 2 if num % 2 == 0 else num ** 3 for num in range(1, 11)]
print(even_squared_odd_cubed)

x_and_y = [(x, y) if x > y else (y, x) for x in range(1, 6) for y in range(1, 6)]
print(x_and_y)

listcomp = [num % 3 for num in range(1, 10)]
setcomp = {num % 3 for num in range(1, 10)}
dictcomp = {k: v for k, v in enumerate("Banke", 0)}
geneexp = (num for num in range(1, 6))

print(type(listcomp), listcomp)
print(type(setcomp), setcomp)
print(type(dictcomp), dictcomp)
print(type(geneexp), geneexp)
print(list(geneexp))

sum_of_x_y = [x + y for x in range(1, 4) for y in range(1, 4)]
print(sum_of_x_y)

check_for_lowercase = [word for word in "The Food Is Here" if word.isupper()]
print(check_for_lowercase)
