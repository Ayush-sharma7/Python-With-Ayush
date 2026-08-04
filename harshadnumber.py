def sumdigit(x):
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s


def harshad(x):
    sd = sumdigit(x)
    if x % sd == 0:
        return 1
    else:
        return 0


# main
a = int(input("enter number: "))
if harshad(a):
    print("given number is harshad number!!")
else:
    print("given number is not a harshad number;(")
