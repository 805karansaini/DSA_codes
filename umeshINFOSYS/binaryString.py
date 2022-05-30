def stringUpdation(s):
    count = 0
    for i in range(len(s)):
        if s[i]=="0":
            count+=1
        else:
            pass
    return count


s1 = "1001"
print("1st Case", stringUpdation(s1))
s2 = "1110"
print("2nd Case", stringUpdation(s2))
s3 = "1000001"
print("3rd Case", stringUpdation(s3))