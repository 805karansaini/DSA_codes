import copy
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(copy.deepcopy(arr[:mid]))
    right = mergeSort(copy.deepcopy(arr[mid:]))
    mix = merge(left,right)
    return mix

def merge(first, second):
    i, j, k = 0, 0, 0
    mix = [0] * (len(first) + len(second))
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            mix[k] = first[i]
            k += 1
            i += 1
        else:
            mix[k] = second[j]
            j += 1
            k += 1
    while i < len(first):
        mix[k] = first[i]
        i += 1
        k += 1
    while j < len(second):
        mix[k] = second[j]
        j += 1
        k += 1
    return mix

arr = [6,5,4,324,4234,53654645,6456467,467,565,876,8,679,564,79,3423,34,5,23,23,42423423423,42343,2,10]
arr = mergeSort(arr)
print(arr)