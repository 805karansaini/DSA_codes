def mergesort(array):
    if len(array) <= 1:
        return
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    mergesort(left)
    mergesort(right)
    merge(left,right,array)

def merge(left,right,array):
    i,j,k = 0,0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i+=1
        else:
            array[k] = right[j]
            j+=1
        k+=1
    
    while i < len(left):
        array[k] = left[i]
        i,k = i+1, k+1
    while j < len(right):
        array[k] = right[j]
        j,k = j+1, k+1



arr = [9,8,7,6,5,4,3,2,1]
mergesort(arr)
print(arr)