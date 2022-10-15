# 5)create three arrays and find the common element in these array
a1=[11,12,13,14,15,16]
a2=[15,16,17,18,19,20]
a3=[15,16,21,22,23,24]
a=(set(a1).intersection(a2).intersection(a3))
print("Common Element is: ",list(a))
