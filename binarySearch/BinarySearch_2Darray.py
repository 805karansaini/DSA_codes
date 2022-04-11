# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
#
# learn how to use mulitple function in a single class
# self.functionname() to call the other function in a class
#  use  how to call function in leetcode using "SELF."

class Solution(object):

    def searchMatrix(self, matrix, target):
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

        return self.searchBS(matrix, target, rEnd)

    def searchBS(self, matrix, target, rNum):

        s = 0
        e = len(matrix[0]) - 1

        while s <= e:
            m = s + (e - s) // 2
            if matrix[rNum][m] == target:
                return True;
            elif matrix[rNum][m] < target:
                s = m + 1
            else:
                e = m - 1
        return False;

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
