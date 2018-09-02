def min_in_four_numbers(x1,x2,x3,x4):
    return min([float(x1),float(x2),float(x3),float(x4)])
array = input().split()
print(min_in_four_numbers(float(array[0]),float(array[1]),float(array[2]),float(array[3])))