num = int(input())
array = []
array = input().split()
count=0
for i in range(0,num,1):
    if int(array[i])>int(array[i-1]) and i!=0:
          count+=1
print(count)