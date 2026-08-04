# power recursion
def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)


a = int(input("enter number: "))
b = int(input("enter exponent: "))
print(power(a, b))
