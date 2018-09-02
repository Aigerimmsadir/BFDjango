num = int(input())
array = []
array = input().split()
count=0
for i in range(1,num-1,1):

    if int(array[i])>int(array[i-1])  :
        if  int(array[i])>int(array[i+1]) :
              count+=1
print(count)