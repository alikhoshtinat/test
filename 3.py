import re
a = input()
b = input()
cnt = 0
while re.search(b,a) != None:
    x = re.search(b,a)
    a = a[(x.span()[0]+1):]
    cnt+=1
print(cnt)