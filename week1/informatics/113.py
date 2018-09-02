import math
num = int(input())
count=1
while(count<=num):
    if int(math.sqrt(count))*int(math.sqrt(count))==count:
        print (count)
    count+=1
