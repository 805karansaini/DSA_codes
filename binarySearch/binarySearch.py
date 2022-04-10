def binarySearch(nums, target):
    start = 0
    last = len(nums) - 1

    while start <= last:
        mid = (start + (last - start) // 2)

        if target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            last = mid - 1
        elif target == nums[mid]:
            return mid
    else:
        return -1



nums1 = [1,2,3,4,5,6,12,12,35,56,67]
target1 = 5

print(binarySearch(nums1, target1))