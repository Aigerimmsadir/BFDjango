k = 0
s = input()
sub = input()
for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        k+=1
print (k)