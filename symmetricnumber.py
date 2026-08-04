def cd(x):
    c = 0
    while x:
        c += 1
        x //= 10
    return c


def sym(x):
    d = cd(x)
    if d % 2 == 0:
        s1, s2 = 0, 0
        for i in range(1, d + 1):
            if i < d / 2:
                s1 += x % 10
                x //= 10
            else:
                s2 += x % 10
                x //= 10
        if s1 == s2:
            return 1
        else:
            return 0
    else:
        return 0


# main
a = int(input("enter upper limit: "))
b = int(input("enter lower limit: "))
c = 0
for i in range(a, b + 1):
    if sym(i):
        c += 1
print("total number of symmetric numbers are: ", c)
