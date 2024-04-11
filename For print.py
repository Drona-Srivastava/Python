# Generate a number between 0 and 10
n=int(input())
print("Range function with stop")
for i in range(n):
    print(i)
print("Range function with start and stop")
for i in range(1,n):
    print(i)
print("Range function with start stop and step")
for i in range(1,n,2):
    print(i)
