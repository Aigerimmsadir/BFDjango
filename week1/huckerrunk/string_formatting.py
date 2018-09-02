def print_formatted(number):
    num=int(number)
    width = len(str(bin(int(number))))+1
    for i in range (num+1):
        s=""
        s+=str(i).rjust(width, ' ')
        s+=str(int(str(i), 8)).rjust(width, ' ')
        s+=str(int(str(i), 16)).rjust(width, ' ')
        s+=str(int(str(i), 2)).rjust(width, ' ')
        print(s)
