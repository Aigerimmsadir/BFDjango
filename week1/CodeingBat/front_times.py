def front_times(str, n):
    s = str[0:3]
    str=str[0:3]
    for i  in range(n-1):
        str+=s
    return str
print(front_times(input(),int(input())))