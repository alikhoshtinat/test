r=0
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        for k in range(j,j+i+1):
            for l in range(1, i+j-k+1):
                r+=1
                #print('*',end='')
            #print()
        #print()
    #print()
print(r)