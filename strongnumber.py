def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


def strong(x):
    s = 0
    a = x
    while x:
        s += fact(x % 10)
        x //= 10
    if s == a:
        return 1
    else:
        return 0


# main
a = int(input("enter number: "))
if strong(a):
    print("given number is strong number")
else:
    print("given number is not strong number")
