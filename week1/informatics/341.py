count=0
num = int(input())
for i in range (2,num+1,1):
    if num%i==0:
        count+=1
print(count)