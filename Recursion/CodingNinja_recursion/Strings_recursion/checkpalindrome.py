def checkpali(s,start,last):
    if last-start < 1 or start == last:
        return True
    elif s[start] != s[last]:
        return False
    return checkpali(s,start+1,last-1)


s = "abaKaba"
print(checkpali(s, 0, len(s)-1))

s = "abaccaba"
print(checkpali(s, 0, len(s)-1))