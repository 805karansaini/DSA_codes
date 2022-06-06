def uniquePathsWithObstacles(obstacleGrid):
    R = len(obstacleGrid)
    C = len(obstacleGrid[0])

    has_cache = [[False] * C for _ in range(R)]
    cache = [[None] * C for _ in range(R)]

    # for a cell x, y, how many ways are there to get to bottom-right
    # x -> 0 to R
    # y -> 0 to C
    # number of inputs = O(R * C)
    # each input takes O(1) time
    # total time is O(R * C)
    def count(x, y):
        if obstacleGrid[x][y] == 1:
            return 0

        if x == R - 1 and y == C - 1:
            return 1

        if has_cache[x][y]:
            return cache[x][y]

        totalPaths = 0
        if x + 1 < R:
            totalPaths += count(x + 1, y)

        if y + 1 < C:
            totalPaths += count(x, y + 1)

        has_cache[x][y] = True
        cache[x][y] = totalPaths
        return totalPaths

    return count(0, 0)

obs = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obs))