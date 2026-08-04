def prime(x):
    c = 1
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return 0
            break
    else:
        return 1


# main
a = int(input("enter lower limit: "))
b = int(input("enter upper limit: "))
for i in range(a, b + 1):
    if prime(i):
        print(i, end=" ")
