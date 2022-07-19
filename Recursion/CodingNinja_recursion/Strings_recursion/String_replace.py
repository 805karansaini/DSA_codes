def replaceXtoY(s,x,y):
    # abcbssdb  s to z -> abcbzzdb
    if len(s) == 0:
        return s
    if s[0] == x:
        return y + replaceXtoY(s[1:],x,y)
    else:
        return s[0] + replaceXtoY(s[1:],x,y)

s = "abcbssdb"
x = "s"
y = "z"
print(s, " -> ",replaceXtoY(s,x,y))

def replacePI(s):
    # abpippidb  pi to "3.14" -> ab3.14p3.14db
    if len(s) == 0 or len(s) == 1:
        return s
    if s[0] == "p" and s[1] == "i":
        return "3.14" + replacePI(s[2:])
    else:
        return s[0] + replacePI(s[1:])

s = "abpippidb"
print(s, " -> ",replacePI(s))

def removeDup(s):
    if len(s)==1:
        return s
    if s[0] == s[1]:
        return removeDup(s[1:])
    else:
        return s[0] + removeDup(s[1:])

s = "xxxyzzzxzbjjksadlls"
print(removeDup(s))