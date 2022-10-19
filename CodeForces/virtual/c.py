
def solve():
    N, s = input().split()
    S = input()
    # print(N)
    # print(s)
    # print(S)
    if s == "g":
        return 0
    answer = 0
    high = len(S)
    for indx, c in enumerate(S):
        if c == "g":
            first = indx
            break

    answer = 0
    flagChar = False
    lastSeenG = 0
    for i in range(high):
        if S[i] == s and not flagChar:
            prev = i
            flagChar = True
        if flagChar and S[i] == "g":
            answer = max(answer, i - prev)
            flagChar = False
        if S[i] =="g":
            lastSeenG = i
    lastSeenS = 0
    # print(high-1, lastSeenG)
    for i in range(high-1,lastSeenG,-1):
        # print(i)
        if S[i] == s:
            lastSeenS = i
    if lastSeenS < lastSeenG:
        return answer
    return max(answer, high+first - lastSeenS)


def solution():
    t = int(input())
    for _ in range(t):
        temp = solve()
        print(temp)
    

solution()