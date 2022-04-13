# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 33. Search in Rotated Sorted Array
# if we choose any MIDDLE in array the array on LEFT( 0 - M) sorted or RIGHT ( M - last ) sorted
# now we can see if the element is in the sorted part or not
# and change the values for START or LAST in Bin. Search Accordingly

def search(nums, target):
    start, last = 0, len(nums) - 1

    while start <= last:

        mid = start + (last - start) // 2
        if nums[mid] == target:
            return mid
        # else check for the sorted array And Inside the sorted array search for target, and change last&start
        elif nums[start] <= nums[mid]:
            if nums[start] <= target <= nums[mid]:
                last = mid - 1
            else:
                start = mid + 1
        elif nums[mid] <= nums[last]:
            if nums[mid] <= target <= nums[last]:
                start = mid + 1
            else:
                last = mid - 1

    return -1;
nums = [4,5,6,7,0,1,2,3]
target = 0
nums1 = [4,5,6,7,0,1,2]
target1 = 3

print("Index ", search(nums,target))
print("Index ", search(nums1,target1))