def palindrome(name):
    if name == name[::-1]:
        print(name," is palindrome")
    else:
        print(name," is not palindrome")
name=input("Enter a string ")
palindrome(name)


