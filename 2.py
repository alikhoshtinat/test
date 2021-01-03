import re
a = input().split('@#')
pat = '@#'
pattern = '^forward,x=(\d*),y=(\d*),distance=(\d*)#@$'
m =[]
for s in a:
    if re.match(pattern,s) != None:
        x = re.match(pattern,s)
        m.append([x.group(1),x.group(2),x.group(3)])
    elif len(s) >=198:
        exit()

