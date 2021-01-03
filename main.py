import math
a = []
b = []
n = int(input())
x = input().split()
a = x
if a != []:

    for i in a :
        b.append(max(a))
        a.remove(max(a))
        b.append(min(a))
        a.remove(min(a))

for i in b:
    print (i , end = " ")