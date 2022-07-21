def quickSort(arr,low,high):
    s = low
    e = high
    if s > e:
        return
    mid = s + (e-s)//2

    while s <= e:
        while arr[s]<arr[mid]:
            s+=1
        while arr[mid]<arr[e]:
            e-=1
        #swap
        if s <= e:
            arr[s] , arr[e] = arr[e], arr[s]
            s+=1
            e-=1
    quickSort(arr,low,mid-1)
    quickSort(arr,mid+1,high)

arr = [2,87,3,25,643,22,234]
quickSort(arr,0,len(arr)-1)
print("final",arr)
arr = [9,342,9342,546,23423849,9,323,453,32345,5667,1,3,4,52,5,3,2]
quickSort(arr,0,len(arr)-1)
print("final",arr)
