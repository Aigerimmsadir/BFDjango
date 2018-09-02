nestedmap={}
n = int(input())
for i in range(0,n,1):
    name= input()
    score = float(input())
    nestedmap.update({name : score})

# for key, value in nestedmap.items():
#     print (key,value)
sortedvalues = sorted(list(map(float, nestedmap.values())))
uniquesortedvalues =[]
for x in sortedvalues:
    if x not in uniquesortedvalues:
        uniquesortedvalues.append(x)
secondlowest = uniquesortedvalues[1]
orderednames=[]
for key, value in nestedmap.items():
     if value==secondlowest:
        orderednames.append(key)
newordered = sorted(orderednames)
for x in newordered:
    print(x)