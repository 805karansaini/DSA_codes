
# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/submissions/
# can run script locally


def searchMatrix( matrix, target):
    row = len(matrix)
    col = len(matrix[0])
    rStart = 0
    rEnd = row - 1

    while rStart <= rEnd:
        mid = rStart + (rEnd - rStart) // 2
        if matrix[mid][0] == target:
            return True;
        elif matrix[mid][0] < target:
            rStart = mid + 1
        else:
            rEnd = mid - 1

    return searchBS(matrix, target, rEnd)

def searchBS(matrix, target, rNum):

    s = 0
    e = len(matrix[0]) - 1

    while s <= e:
        m = s + (e - s) // 2
        if matrix[rNum][m] == target:
            return True;
        elif matrix[rNum][m] < target:
            s = m + 1
        else:
            e = m -1
    return False;


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60], [123,130,134,160],[223,230,234,260]]
target = -1
print(searchMatrix(matrix,target))