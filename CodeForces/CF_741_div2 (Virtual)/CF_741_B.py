from collections import Counter
def solve():
    seen = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])
    def helper2(s):
       # print("inside helper 2")
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                temp = int(s[i] + s[j])
                #print(temp)
                if temp not in seen:
                    print("2")
                    print(temp)
                    return True
        return False
    
    def helper3(s):
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                for k in range(j+1,len(s)):
                    temp = int(s[i] + s[j] + s[k])
                    if temp not in seen:
                        print("3")
                        print(temp)
                        return True

    t = int(input())
    while t:
        t-=1
        n = int(input())
        s = input()
        count = Counter(s)
        if "1" in count:
            print("1")
            print("1")
            continue
        
        if "4" in count:
            print("1")
            print("4")
            continue
        
        if "6" in count:
            print("1")
            print("6")
            continue
        
        if "8" in count:
            print("1")
            print("8")
            continue
        if "9" in count:
            # print(count)
            print("1")
            print("9")
            continue

        if "2" in count:
            if count["2"] > 1:
                print("2")
                print("22")
                continue
        if "7" in count:
            if count["7"] > 1:
                print("2")
                print("77")
                continue
        if "5" in count:
            if count["5"] > 1:
                print("2")
                print("55")
                continue
        if "3" in count:
            if count["3"] > 1:
                print("2")
                print("33")
                continue
        help = False
        #print("helper")
        help = helper2(s)
        if not help:
            helper3(s)
        continue
            
solve()