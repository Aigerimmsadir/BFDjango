num = int(input())
array = []
array = input().split()
s=""
for i in range(0,num,1):
    if i%2==0:
        s+=str(array[i])
        s+=' '
print(s)