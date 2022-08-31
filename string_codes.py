import math

minute = 5
arg = 'Argument'
s = "sorry,is this the {} minute {}?" .format(5, 'Argument') # or
# s = f"Sorry is this the {minute=} minute {arg=}?"

print("{:^10} is {:.2f} years old".format("Bill", math.pi * 100))
print(s)

for i in range(1, 11):
    sym = "*" * i
    print('{:>10}'.format(sym))

    # print(f'{sym:>10}')


