import math as m


def cd(x):
    s = 0
    while x:
        s += 1
        x //= 10
    return s


def armstrong(x):
    s = 0
    a = x
    d = cd(x)
    while x:
        s += m.pow(x % 10, d)
        x //= 10
    if s == a:
        return 1
    else:
        return 0


# main
a = int(input("enter lower range: "))
b = int(input("enter upper range: "))
for i in range(a, b + 1):
    if armstrong(i):
        print(i, end=" ")
