number: int = int(input("Enter a number: "))

something = False

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            something = True
            break

if something:
    print(number, "is not a prime number")
else:
    print(number, "is a prime number")


# for i in range(10, 0, -1):
#     print(i)