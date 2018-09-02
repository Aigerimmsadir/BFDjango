num1 = int(input())
num2 = int(input())
s=""
for i in range(num1,num2,1):
    if i%2==0:
        s+=str(i)
        s+=" "
print(s)