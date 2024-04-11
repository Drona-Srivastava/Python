summ=[]
final=[]
name2=[]
number=int(input('number: '))
for i in range(0,number):
    name = input('name: ')
    score = float(input('marks: '))
    combo=[name,score]
    final.append(combo)
for i in range(0,len(final)):
    num=final[i]
    num1=num[1]
    name1=num[0]
    summ.append(num1)
    name2.append(name1)
summ.sort()
i1=summ[len(summ)-3]
i2=summ[len(summ)-4]
for i in range(0,len(final)):
    no=final[i]
    while i1==no[1] and i2==no[1]:
        print(no[0],end=" ")
        
print(i1,i2)    