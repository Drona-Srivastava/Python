'''Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.'''
n = int(input("Enter number of inputs: "))
integer_list = map(int, input('Enter Number: ').split())
tup=tuple(integer_list)
print(tup)
print(hash(tup))

