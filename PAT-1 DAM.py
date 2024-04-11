#PAT-1 DAM
cap=int(input('Enter total capacity: '))
n=int(input('Enter the total number of inputs: '))
lit=[]
mil=[]
for i in range(0,n):
    ltr=int(input('Enter the litres: '))
    mili=int(input('Enter the mili-litres: '))
    lit.append(ltr)
    mil.append(mili)
ltrf=sum(lit)
miln=sum(mil)
if miln>1000:
    litf1=ltrf+miln//1000 #Converting mL to L and getting total L
    milf=int(((ltrf+miln/1000)-litf1)*1000) #Getting mL
else:
    milf=miln
    litf1=ltrf
if litf1>cap:
    print('DAM_IN_DANGER')
elif litf1==cap:
    print('DAM_IS_FULL')
else:
    print('DAM_IS_EMPTY')