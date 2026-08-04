def sumdigit(x):
    sum = 0
    while x:
        sum += x % 10
        x //= 10
    return sum


# main
num = int(input("enter number: "))
sum = sumdigit(num)
while True:
    if sum - 10 >= 0:
        sum = sumdigit(sum)
    else:
        print(sum)
        break
