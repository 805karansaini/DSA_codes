# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix
# 1351. Count Negative Numbers in a Sorted Matrix
# how to approach
# set target anything (in this case set it to -1)
# do binary search for the -1 (so the start becomes closest to -1)
# in this Question sorted in 9, 8, 7, 0,-1, -1, -1, -2, -3 i.e. decreasing order
# so search for -1. then  start ... mid ... last will reduce the space so that -1 can be found
# let say Array is this at some point of time 0, -1, -1, -1, -2
# m = 2 nums[m] = -1 but at index 2.       I.E.     0, -1, (-1,) -1
# again reduce the space l = m-1.  So s=0 l=1
# now we can see we will START will be RETURNED. when our condition breaks

def countNegatives(grid):
    r = len(grid)
    c = len(grid[0])
    index = len(grid[0])-1
    count = 0

    for i in range(r):
        start = 0
        last = c-1

        if grid[i][last] >= 0:
            count = count
            continue
        while start <= last:
            mid = start + (last - start)//2
            if grid[i][mid] < -1:
                last = mid - 1
            elif grid[i][mid] > -1:
                start = mid + 1
            elif grid[i][mid] == -1:
                last = mid - 1

            # if grid[i][mid] <= -1:
            #     last = mid - 1
            # else:
            #     start = mid + 1

        count = count + index - start + 1


    return count


nums = [[4,3,2,-1],[3,-1,-10,-30],[1,0,-1,-2],[-1,-10,-20,-30]]

# nums = [[3,2],[1,0],[2,3],[-1,-2]]
print(countNegatives(nums))