def buzzno(x):
    if x % 10 == 7:
        print(x, "is a buzz number")
    elif x / 7 == 0:
        print(x, "is a buzz number")
    else:
        print(x, "is not a buzz number")


a = int(input("enter a number"))
buzzno(a)
