a = input()
mylist = [] #3 2 1
while a != '0':
    mylist.append(a)
    a = input()
i = len(mylist)-1
while i>= 0:
    print(mylist[i])
    i-=1