a = int(input("enter number of rows: "))
c = 1
for i in range(1, a + 1):
    for j in range(i):
        print(c, end=" ")
        c += 1
    print()
