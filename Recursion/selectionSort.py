#select the max elements for n elements put it at thr place of nth element similarly
#select the max elements for n-1 elements put it at thr place of n-1 th element
#select the max elements for n-2 elements put it at thr place of n-2 th element


def selectionSort(arr,index,n,maxIndex):
    if index == 0:
        return
    if index > n:
        if arr[n] > arr[maxIndex]:
            selectionSort(arr,index,n+1,n)
        else:
            selectionSort(arr,index,n+1,maxIndex)
    else:
        #swap max
        temp = arr[maxIndex]
        arr[maxIndex] = arr[index-1]
        arr[index-1] = temp
        selectionSort(arr,index-1,0,0)





arr = [4,1,32,432,4654,32,5,6,7,8,9,12]
#selectionSort(arr,index,n,maxIndex)
selectionSort(arr,len(arr),0,0)
print(arr)