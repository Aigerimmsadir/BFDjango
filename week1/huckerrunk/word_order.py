n = int(input())
occ={}
arr=[]
count=0
for i in range(0,n,1):
    s=input()
    if s not in arr:
        arr.append(s)
        occ[s]=1
        count+=1
    else: occ[s]+=1
s =""
print(count)
for key,value in occ.items():
    print(value,end=' ')
