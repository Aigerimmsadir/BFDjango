def max_end3(nums):
    maxx = max(nums)
    nums[0]=maxx
    nums[1]=maxx
    nums[2]=maxx
    return nums
print(max_end3(input().split()))