def love6(str1, str2):
    a=int(str1)
    b=int(str2)
    if abs(a)==6 or abs(b)==6 :
        return True
    elif a+b==6 or abs(a-b)==6:
        return True
    elif abs(b-a)==6:
        return True
        return True
    return False