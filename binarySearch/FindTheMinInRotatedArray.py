# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
# HOW TO APPROACH IT
# if nums[mid] < nums[last] it means that array is sorted form mid to last and we can change LAST = MID
# include i.e. Last = MID as (nums[mid] can be the answer.
# else if nums[mid] > nums[last] we can say that nums[last] is already smaller than the nums[mid]
# therefore, we can search in the start = Mid+1 (as nums[mid] is already not the solution
# return :  we can RETURN any LAST , START index as Loop only breaks when both are the same.

def findMin(nums):
    start = 0
    last = len(nums ) -1

    while start < last:
        mid = start + (last -start )//2
        if nums[mid] > nums[last]:
            start = mid + 1
        if nums[mid] < nums[last]:
            last = mid

    return start


nums = [10,13,19,20,-18,-11,4,5,6,7,8,9]
i = findMin(nums)
print(nums[i])
