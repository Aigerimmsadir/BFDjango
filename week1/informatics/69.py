num = int(input())
array = []
array = input().split()
s=""
for i in reversed(array):
    s+=i
    s+=" "
print(s)