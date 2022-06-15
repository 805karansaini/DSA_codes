from collections import defaultdict
from collections import Counter
def solve():
    t = int(input())
    while t:
        t-=1
        hhmm = input().split()
        min = int(hhmm[1])
        time = hhmm[0].split(":")
        hh = time[0]
        mm = time[1]
        hhadd = min//60
        mmadd = min%60
        time_gone = int(hh)*60 + int(mm)
        total_time = 60 * 24
        count = 0
        seen = defaultdict(int)
        dic = defaultdict(int)
        tempseen = "" + hh + mm
        while tempseen not in seen:
            print(tempseen)
            print(seen)
            print(dic)
            if len(hh)==2:
                pass
            else:
                hh = "0" + hh
            if len(mm) == 2:
                pass
            else:
                mm = "0" + mm
            if hh == mm[::-1]:
                tempdic = "" + hh + mm
                if tempdic not in dic:
                    dic[tempdic] = 1
                    count += 1
            tempseen = hh + mm
            seen[tempseen] = 1
            tempmm = (int(mm) + mmadd) % 60
            temphhadd = (int(mm) + mmadd) // 60
            temphh = (int(hh) + hhadd + temphhadd) % 24
            if len(temphh)==2:
                pass
            else:
                temphh = "0" + temphh
            if len(tempmm) == 2:
                pass
            else:
                tempmm = "0" + tempmm
            hh = str(temphh)
            mm = str(tempmm)
            tempseen = "" + hh + mm
        print(count)
    return
solve()