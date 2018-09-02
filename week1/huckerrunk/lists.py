list=[]
n = int(input())
for i in range (n):
    a = input().split()
    if(len(a)==3):
        list.insert(int(a[1]),int(a[2]))
    elif(len(a)==2 and a[0]=="remove"):
        list.remove(int(a[1]))
    elif(len(a)==2 and a[0]=="append"):
        list.append(int(a[1]))
    elif ( a[0] == "print"):
        print(list)
    else: eval("list." + a[0] + "()")

