def partition(arr, low, high):
    mid = low  + ( (high-low)//2 )
    # linear search to get index of pivele if any value is samller and equal to pivele it will be on left side
    count = 0
    for i in range(low, high+1):
        if arr[i] <= arr[mid]:
            count += 1
    temp = low+count-1
    # putting arr[mid] at right index 
    arr[mid], arr[temp] =  arr[temp], arr[mid]

    # swaping values if any value is smaller or equal to pivele it will be on left side
    while low < high:
        while arr[low] <= arr[temp]:
            low += 1
        while arr[high] > arr[temp]:
            high -= 1
        if arr[low] > arr[temp] and arr[high] < arr[temp]:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    return temp
    

def quicksort(arr,low,high):
    if low >= high:
        return 
    mid = low  + ( (high-low)//2 )

    pivot = partition(arr,low,high)
    quicksort(arr,low,pivot-1)
    quicksort(arr,pivot+1,high)

arr = [9,342,9342,546,23423849,9,323,453,32345,5667,134]
quicksort(arr,0,len(arr)-1)
print(arr)
print(sorted(arr))