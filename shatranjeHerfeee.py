mylist = [1,1,2,2,2,8]
inputlist = input().split()

for i in range(0,6):
    inputlist[i] = int(inputlist[i])
    print(mylist[i] - inputlist[i], end=' ')
