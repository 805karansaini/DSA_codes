from collections import Counter
def solve():
    t = int(input())

    while t:
        t-=1
        pas = input()
        board = [None]*8
        i = 0
        for i in range(8):
            row = input()
            board[i] = row

        res = []
        for i in range(0,8):
            count = Counter(board[i])
            if count["#"]==2:
                for j in range(0,8):
                    if "#"==board[i][j]:
                        res.append([i + 1, j + 1])
                break
        # print(res)
        if len(res)==1:
            l, m = res[0]
            print(l,m)
        else:
            for i in range(1,8):
                l = res[0][0] + i
                m = res[0][1] + i
                n = res[1][0] + i
                o = res[1][1] - i
                if l==n:
                    if m == o:
                        print(l,m,)
                        break
    return
solve()