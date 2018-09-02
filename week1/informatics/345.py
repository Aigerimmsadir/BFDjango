num = int(input())
count=0
for i in range (num):
    num1 = input()
    for j in range(len(num1)):
        if num1[j]=="0":
            count+=1
print(count)