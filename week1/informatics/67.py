num = int(input())
array = []
array = input().split()
count=0
for i in range(0,num,1):
    if int(array[i])*int(array[i-1])>0 and i!=0:
        print("yes")
        count=1
        break
if count==0:
    print("no")