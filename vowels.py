para=input("Enter a paragraph")
vowels=('a','e','i','o','u')
count=0
for i in para:
    if i in vowels:
        count=count+1
if count>=1:
    print(count,"vowels")
else:
    print("no vowels")

