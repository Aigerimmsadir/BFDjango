def sum3(nums):
    count =0
    for i in nums:
        count+=int(i)
    return count
print (sum3(input().split()))