def xor(x,y):
    if(int(x)*int(y)==0 and int(x)+int(y)==1) : return 1
    return 0
arr = input().split()
print(xor(arr[0],arr[1]))
