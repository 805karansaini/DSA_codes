
def solve():
    t = int(input())
    while t:
        t-=1
        F,S = input().split()
        
        if F == S:
            print("=")
            continue

        size1, size2 = F[-1], S[-1]
        dic = { "S": 1, "M" : 2, "L":3}
        if dic[size1] > dic[size2]:
            print(">")
        elif dic[size1] < dic[size2]:
            print("<")
        else:
            if size1 == "S":
                if len(F) > len(S):
                    print("<")
                else:
                    print(">")
            else:
                if len(F) > len(S):
                    print(">")
                else:
                    print("<")


        

        
  
solve()