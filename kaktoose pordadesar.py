n = int(input())
mylist = input().split()
for a in mylist:
    a = int(a)
    if a <=3:
        print(a*'*')
    else:
        print('*')