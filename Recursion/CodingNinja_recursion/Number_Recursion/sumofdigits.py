from tkinter import N


def sumofdigits(n):
    temp = n%10
    rem = n//10
    if rem == 0:
        return temp
    return temp + sumofdigits(rem)

n = 156723
print(sumofdigits(n))

n = 3247874287349
print(sumofdigits(n))