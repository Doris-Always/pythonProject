number: int = int(input("Enter a number and get the factorial: "))
factorial = 1
if number < 0:
    print("input a positive number")
elif number == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print("factorial of the number is", factorial)
