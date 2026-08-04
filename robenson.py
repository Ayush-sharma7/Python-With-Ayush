a = 1
b = 0
x = 0
c = int(input("enter value:"))
c = x
while c != 0:
    r = c % 10
    for i in range(1, r + 1):
        a = a * i
    b = b + a
    c = c // 10
if b == x:
    print("robenson")
else:
    print("not")
