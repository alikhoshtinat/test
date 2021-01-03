import re
a = input()
b = input()
b +="='(\S*)'"
x = re.findall(b,a)
for i in x:
    print(i)
