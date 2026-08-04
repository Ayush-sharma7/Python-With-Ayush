def factor(x):
    b = ""
    for i in range(2, x + 1):
        while x % i == 0:
            x = x // i
            b = b + str(i) + "*"
    return b[: len(b) - 1]


# main
a = int(input("enter value:"))
print(factor(a))
