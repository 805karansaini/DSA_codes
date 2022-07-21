def tower_hanoi(n,src, aux, des):
    if n == 1:
        print("Move the 1st disk form", src, " to ", des)
        return
    tower_hanoi(n-1,src, des, aux)
    print("Move the", n,"th disk form", src, " to ", des)
    tower_hanoi(n-1,aux, src, des)

tower_hanoi(1, "src", "aux", "des")
print()
tower_hanoi(2, "src", "aux", "des")
print()
tower_hanoi(3, "src", "aux", "des")