def bubbleSort(arr, r, c):
    if r == 0:
        return
    if c < r:
        #swap
        if arr[c] > arr[c+1]:
            temp = arr[c+1]
            arr[c+1] = arr[c]
            arr[c] = temp
        bubbleSort(arr,r,c+1)
    else:
        bubbleSort(arr,r-1,0)




arr = [4,3,2,1]

bubbleSort(arr,len(arr)-1,0)
print(arr)