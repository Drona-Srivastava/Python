n=int(input())
x=1
y=1
while n!=0:
    for i in range(1,y+1):
        for j in range(1,y+1):
            print(x, x,end=' ')
            x+=1
            y+=1
            n-=1
        print()