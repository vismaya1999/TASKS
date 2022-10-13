# n=int(input("Enter any number: "))
# if n>1:
#     for i in range(2,n+1):
#         if n%i==0:
#             print("Not a Primeno.")
#             break
#         else:
#             print("Prime No.")
#
#


def prime(n):
        for i in range(2,n+1):
            if n%i==0:
                print(n," Not a Prime")
                break
            else:
                print(n," is Prime no")
                break

n=int(input("Enter a number "))
prime(n)

