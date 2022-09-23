def longestContinuousSubstring(s):
        N = len(s)
        seen = set()
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alpha)):
            for j in range(i,len(alpha)):
                # print(i,j)
                seen.add(alpha[i:j+1])
        # print(seen)
        best = 1
        i = j = 0
        N = len(s)
        while i < N:
            while j < N:
                if s[i:j+1] in seen:
                    j += 1
                    # print(s[i:j],i, j , " machin")
                    if j-i+1 > best:
                        best = j-i
                        if best == 26:
                            return best
                else:
                    break
            if j > i:
                i = j
            else:
                i += 1

        return best
for i in range(4):
    print(longestContinuousSubstring(input()), " answer")