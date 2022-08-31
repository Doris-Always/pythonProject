word =(input("Enter...: "))

if word[::-1] == word[::1]:
    print(word, " is a palindrome")
else:
    print(word, "is not a palindrome")
