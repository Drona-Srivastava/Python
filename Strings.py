# Functions of string
str='Welcome to SCOPE'
print(str)
print(str[0])
print(str[3:7])
print(str[3:])
print(str*2)
print(str[11:16]*3)
print(str+'VIT CHENNAI')
lis1=[13,13,324]
adlnc=set(lis1)
print(adlnc)
print(list(adlnc))
name=('Drona              Sri')
list1=list(name.split())
print(list1)
print(' '.join(list1)) #adds the character between the list elements 
for i in list1:
    print(i,end=" ")# same as join but with for loop
string1='     sri      drona     sri      '
print(string1.find('sri'), '#gives first occurence' ,string1.capitalize() ,'#First letter capatilization', string1.lstrip('drona') ,'#removes lest space' ,string1.rstrip('drona') ,'#removes right space' ,string1.strip('sri') ,'#removes space from both side')
print(string1.upper())
print(string1.lower())
print(string1.title())
name2='Drona'
print(name2.swapcase())
