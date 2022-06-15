from collections import defaultdict
def solve():
    t = int(input())
 
    while t:
        t-=1
        time, mins = [*map(str, input().split())]
        mins = int(mins)
        hh, mm = map(int, time.split(":"))
        seen = set()
        curr = hh*60 + mm
        count = 0
        while curr not in seen: 
            # print(seen)
            seen.add(curr)
            hh = curr//60
            mm = curr%60
            s = str(hh//10) + str(hh%10) + str(mm//10) + str(mm%10)
            if s == s[::-1]:
                count += 1   
            curr = (curr + mins) % 1440
        print(count)
    return 
solve()