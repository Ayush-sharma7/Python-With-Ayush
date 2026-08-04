# HAPPY NUMBER: 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100
def sq(x):
    s = 0
    while x:
        s += (x % 10) ** 2
        x //= 10
    return s


a = int(input())
l = []
l.append(a)
s = 0
while s not in l:
    if sq(a) == 1:
        print("True")
        break
    else:
        l.append(sq(a))
        a = sq(a)
        s = sq(a)
else:
    print("False")
