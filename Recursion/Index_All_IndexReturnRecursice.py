def first_index(nums,tar,i):
    if tar == nums[i]:
        return i
    if i == len(nums)-1:
        return -1
    return first_index(nums,tar,i+1)

nums = [0,1,2,3,4,5,6,7,8,9,10,11]
print(first_index(nums,3,0))

def last_index(nums,tar,i):
    if tar == nums[i]:
        return i
    if i == -1:
        return -1
    return last_index(nums,tar,i-1)



nums = [0,1,2,3,4,5,3,6,7,8,9,10,11]
print(last_index(nums,3,len(nums)-1))

def All_index(nums,tar,i,list):
    if tar == nums[i]:
        list.append(i)
    if i == len(nums)-1:
        return list
    return All_index(nums,tar,i+1,list)


nums = [0,1,2,3,4,3,5,6,7,8,9,10,11]
print(All_index(nums,3,0,list = []))


def All_index2(nums,tar,i):
    lis = []
    if i == len(nums):
        return lis
    if tar == nums[i]:
        lis.append(i)
    ans = All_index2(nums,tar,i+1)
    lis = lis + ans
    return lis


nums = [0,1,2,3,4,3,5,6,7,8,9,10,11]
print(All_index2(nums,3,0))