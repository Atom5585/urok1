def palindrome():
    a = input()
    if a == a[::-1]:
        print("True")
    else:
        print("False")
palindrome()
