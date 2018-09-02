# find runner-up
n =int(input())
array=[]
inp=input().split()

for i in range(0,n,1):
    if inp[i] not in array:
        array.append(inp[i])
arraysorted = list(map(int, array)) # list(map(int, strlist)) on Python 3
newarraysorted = sorted(arraysorted)
print(newarraysorted[len(newarraysorted)-2])