def string_times(str, n):
    s=str
    for i in range(n-1):
        str+=s
    return str
print(string_times(input(),3))
