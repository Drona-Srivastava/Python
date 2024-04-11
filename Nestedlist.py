'''Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) 
of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''
num=int(input('Enter the number of records: '))
final=[]
marks=[]
sub=[]
for i in range(num):
    per=[]
    name = input('Enter the name: ')
    score = float(input('Enter the marks: '))
    per.append(name)
    per.append(score)
    marks.append(score)
    final.append(per)
marks.sort()
markset=set(marks)
marks=list(markset)
marks.remove(min(marks))
    
for i in range(0,len(final)):
    if marks[0]==final[i][1]:
        sub.append(final[i][0])
sub.sort()
for j in sub:
    print(j)