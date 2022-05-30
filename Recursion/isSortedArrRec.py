

def isSortedArrRec(nums,i,n):

    if i < n-1:
        if nums[i] < nums[i+1]:
            return isSortedArrRec(nums,i+1,n)
        else:
            return False
    return True


arr = [1,2,3,4,5,6,7,8,9,11,10,12,13,14,15,17,16]
print(isSortedArrRec(arr,0,len(arr)))