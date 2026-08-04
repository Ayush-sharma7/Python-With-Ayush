import math


def cd(x):
    c = 0
    while x:
        c += 1
        x //= 10
    return c


# main
a = int(input("enter number: "))
d = cd(a)
s = 0
i = a
while i:
    c = i % 10
    s = s + math.pow(c, d)
    i = i // 10
if a == s:
    print("the given number is armstrong!!")
else:
    print("not an armstrong number!!")
