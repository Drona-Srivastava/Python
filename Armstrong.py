#Armstrong Number
num=input("Enter the number:")
l=len(num)
dig=list(set(num))
arr=list(map(int,dig))
summ=0
for i in range(0,l):
    summ=summ+arr[i]**l
if int(num)==summ:
    print('The number is an Armstrong number')
else:
    print('The number is not an Armstrong number')
