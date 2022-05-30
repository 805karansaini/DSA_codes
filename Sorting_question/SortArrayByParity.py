
def sortArrayByParity(nums):
    ans = [0 for i in nums]
    s,l = 0, len(nums)-1
    i,j = 0,len(nums)-1

    if s==l:
        return nums

    while s <= l:
        if nums[s]%2==0:
            ans[i]=nums[s]
            s+=1
            i+=1
        else:
            ans[j] = nums[s]
            s += 1
            j -= 1

        if s<l:
            if nums[l]%2==0:
                ans[i]=nums[l]
                l-=1
                i+=1
            else:
                ans[j] = nums[l]
                l -= 1
                j -= 1

    return ans



nums = [0,2,4]
print(sortArrayByParity(nums))

