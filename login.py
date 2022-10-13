# Login
user=["vismaya","sreema","vishnupriya"]
pass1=[1234,5678,2345]
name=input("Enter your Name: ")
if name in user:
    password=int(input("Enter password:  "))
    ind=user.index(name)
    if password in pass1 and ind==pass1.index(password):
        print("Welcome")
    else:
        print("Invalid password")
else:
    print("Invalid Username")
