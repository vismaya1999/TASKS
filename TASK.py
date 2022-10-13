# -----------------------------------------------------------------------------------------------------------------------------
# TASK1
# Write a program which will find all such numbers which are divisible by 7 but are not multiple of 5,
# between 2000 and 3000(both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line::

# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         print(i,end=",")

# OR

# l = []
# for i in range(2000,3201):
#     if i % 7 == 0 and i % 5 != 0:
#         l.append(str(i))
# print(','.join(l))
#

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------
# TASK2

# With a given integral number n, write a program to generate a dictionary that contains(i,i*i)such that is an integral
# number between 1 and n(both included) then the program should print the dictionary
# suppose the following input is 5
# then the output is {1:1,2:4,3:9,4:16,5:25}

# OR

# Define fn which can print a dict where the keys are no. btw 1 and 20 (both are included) and value are sq(key)

# d={}
# n=int(input ('Enter input: '))
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)

# ------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------
# TASK3

## Write a program which can compute the factorial of given numbers
# Suppose the given input is 8 then output should be 40320
# def fact1():
#     n = int(input('Enter input: '))
#     f = 1
#     for i in range(1, n+1):
#         f = f*i
#     print(f)
# fact1()

# ---------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------
# TASK4

# Write a program which accept a sequence of comma separated numbers form console and generate a list and tuple which
# contains every numbers.

# n=input('Enter input ')
# l=n.split(',')
# t=tuple(l)
# print(l)
# print(t)

# -----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------
# TASK5

# Write a program that accepts a sentence and calculate number of uppercase and lowercase letters

# n=input('Enter a string: ')
# up=0
# low=0
# for i in n:
#     if i.isupper():
#         up=up+1
#     elif i.islower():
#         low=low+1
# print("No of uppercase: ",up)
# print("No of lowercase: ",low)

# --------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# TASK6

## Write a program that compute the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as D 100 ,W 200:: D is deposit min deposit 100 and W is withdraw min withdraw 200
# D 900
# W 500
# D 100
# Bal 500


# balance=0
# while True:
#     inp = input("Enter Transaction Details:  ")
#     t=inp.split()
#     trans=int(t[1])
#     if (t[0]=="D" or t[0]=="d") and trans > 100:
#         balance = balance + trans
#         print("Available Balance: ",balance)
#     elif (t[0]=="W" or t[0]=="w") and trans > 200:
#         balance = balance - trans
#         print("Available Balance: ")
#     else:
#         pass
#     step=input("To continue transaction Enter Y ")
#     if step=="Y" or step=="y":
#         continue
#     else:
#         break
# print("Available Balance: ",balance)

# ------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# TASK7

# n=input("Enter count: ")
# values=input("Enter values: ")
# l=[]
# values.split()
# l.append(values)
# print(l)

# -------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------
# TASK8

# item =([10, 20, 30, 40, 10, 10, 50, 30, 40, 30])
# n = int(input("Enter the no to check: "))
# c = 0
# for i in item:
#     if i == n:
#         c = c+1
# print(c)

# ------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------
# TASK9

# Define function that can accept 2 string as input and print the maximum length in console if the string are same length,
# then function should print line by line

# def max(s1,s2):
#     l1=len(s1)
#     l2=len(s2)
#     if l1<l2:
#         print("maxlength: ",l2)
#     elif l1>l2:
#         print("maxlength",l1)
#     else:
#         print(s1)
#         print(s2)
# s1=input("Enter String one: ")
# s2=input("Enter string two: ")
# max(s1,s2)

# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------
# TASK10

# Define fn which can generate a list where the value are square no. btw 1 to 20(both included) then the fn need to
# print last 5 element in the list
# def l1():
#     l=[]
#     for i in range(1,21):
#         l.append(i*i)
#     print(l[-5:])
# l1()

# -------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------
# TASK11

# Write a Python program to find a list of integers with exactly two occurrences of nineteen
# and at least three occurrences of five
# Input:
# [19, 19, 15, 5, 3, 5, 5, 2]
# Output:
# True

# n=int(input('enter the range'))
# a=[]
# for i in range(0,n):
#     b = int(input('Enter values: '))
#     a.append(b)
# print(a)
# if a.count(19)==2 and a.count(5)>=3:
#     print(True)
# else:
#     print(False)

# ------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------
# TASK12

# Write a Python program to find a pair with highest product from a given array of integers.
# Examples :
# Input: arr[] = {1, 2, 3, 4, 7, 0, 8, 4}
# Output: {7,8}
# Input: arr[] = {0, -1, -2, -4, 5, 0, -6}
# Output: {-4, -6}

# a={1, 2, 3, 4, 7, 0, 8, 4}
# OR
# a={0, -1, -2, -4, 5, 0, -6}
# d=list(a)
# arr=len(d)
# def max(arr):
#     x = d[0]
#     y = d[1]
#     for i in range(0,arr):
#         for j in range(i+1,arr):
#             if d[i]*d[j]>x*y:
#                 x=d[i]
#                 y=d[j]
#                 s={x,y}
#     return s
#
# print(max(arr))

# -----------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# TASK13

# Write a Python program that accept a list of integers and check the length and the fifth element.
# Return true if the length of the list is 8 and fifth element occurs thrice in the said list. Go to the
# editor
# Input:
# [19, 19, 15, 5, 5, 5, 1, 2]
# Output:
# True
# Input:
# [19, 15, 5, 7, 5, 5, 2]
# Output:

# n=int(input('Enter range: '))
# l=[]
# if n==8:
#     for i in range(0,n):
#         a = input("values ")
#         l.append(a)
#     print(l)
#     if l.count(l[4])==3:
#         print(True)
#     else:
#         print(False)
# else:
#     print("bye")
#

# -----------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# TASK10

# Have the function ArrayChallenge(arr) take the array of numbers stored in arr which will contain
# integers that represent the amount in dollars that a single stock is worth,and return the maximum
# profit that could have been made by buying stock on day X and selling stock on day Y where Y>X .For
# example if array is [44,30,24,32,35,30,40,38,15] then your program should return 16 because at
# index 2 the stock was worth $24 and at index 6 the stock was then worth $40, so if you brought the
# stock at $24 and sold it at $40, you would have made a profit of $16,which is the maximum profit
# that could hve been made with this list of stock prices.
# If there is no profit that could have been made with the stock prices,then your program should
# return -1. For example arr is [10,9,8,2] then your program should return -1
#
# Example
# Input: [10,12,4,5,9]
# Output:5
#
# arr = [44, 30, 24, 32, 35, 30, 40, 38, 15]
# n=len(arr)
# l=[]
# for i in range(0,n):
#     for j in range(i+1,n):
#         if arr[j]>arr[i]:
#             m=arr[j]-arr[i]
#             l.append(m)
#         else:
#             l.append(-1)
# print(max(l))

# ---------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------
# TASK11

# Python program to display all integers within the range 100-200 whose sum of digits is an even number:
# l=[]
# for i in range(100,201):
#     i = str(i)
#     sum = 0
#     for j in i:
#         j = int(j)
#         sum = sum+j
#     if sum % 2 == 0:
#         l.append(i)
# print(l)

# ------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------
# Task12

# Python program to find the largest number and its position in a list without using bult in function.

# using built in functions;
# l=[1,2,3,14,5,6,7,8,9,10]
# p=[]
# n=len(l)
# for i in range(0,n):
#     for j in range(i+1,n):
#         if l[i]>l[j]:
#             m=l[i]
#             p.append(m)
#         elif l[i]<l[j]:
#             m=l[j]
#             p.append(m)
#         else:
#             pass
# ind=max(p)
# print(l.index(ind))

# l=[]
# n=int(input('Enter range: '))
# for i in range(0,n):
#     m=int(input())
#     l.append(m)
l=[1,2,3,14,5,6,7,8,9,10]
max=l[0]
p=len(l)
for i in range(0,p):
    if max<l[i]:
        max=l[i]
        ind=i
print(ind)