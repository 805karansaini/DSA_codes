def recBin(array, s, e, target):
    if s > e:
        return -1
    mid = s + ((e-s)//2)
    if array[mid] == target:
        return mid
    if array[mid] < target:
        return recBin(array, mid+1, e, target)
    else:
        return recBin(array, s, mid-1, target)
array = [1,2,3,4,5,6,7,8,9,10]
print(recBin(array,0,len(array),6))
print(recBin(array,0,len(array),10))
print(recBin(array,0,len(array),1))
print(recBin(array,0,len(array),0))