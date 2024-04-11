'''The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.'''
n = int(input('Enter no. of records: '))
stu = {}
k=[]
for i in range (0,n):
    k=[]
    som=input('Enter record: ')
    k=som.split()
    name=k[0]
    dum=(float(k[1]),float(k[2]),float(k[3]))
    stu[name]=list(dum)
    
query=input('Enter the query name: ')
if query in stu:
    marks=stu[query]
    per=(sum(marks))/3
    print("{:.2f}".format(per))