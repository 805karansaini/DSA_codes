# https://www.youtube.com/watch?v=nCNfu_zNhyI&ab_channel=codebasics
def mergeSort(arr):
    if len(arr)<=1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    merge(left, right, arr)


def merge(left, right, arr):
    i, j, k = 0, 0, 0
    len_l = len(left)
    len_r = len(right)
    while i < len_l and j < len_r:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        if left[i] > right[j]:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1


arr = [9,8,7,6,5,4,3,2,1]
mergeSort(arr)
print(arr)