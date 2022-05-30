def RotatedBS(nums,tar,s,l):
    if s > l:
        return -1

    mid = s + (l-s)//2
    if nums[mid]==tar:
        return mid
    if nums[s] < nums[mid]:
        if nums[s] <= tar <= nums[mid]:
            return RotatedBS(nums,tar,s,mid-1)
        else:
            return RotatedBS(nums,tar,mid+1,l)
    else:
        if nums[mid] <= tar <= nums[l]:
            return RotatedBS(nums,tar,mid+1,l)
        else:
            return RotatedBS(nums,tar,s,mid-1)


nums = [4,5,6,7,1,2,3]
print(RotatedBS(nums,2,0,len(nums)-1))
print(RotatedBS(nums,4,0,len(nums)-1))
print(RotatedBS(nums,3,0,len(nums)-1))
print(RotatedBS(nums,11,0,len(nums)-1))
