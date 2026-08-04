def bubblesort(l):
    for i in range(a - 1):
        for j in range(a - i - 1):
            if l[j] < l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


a = int(input("enter number of elements: "))
l = []
for i in range(a):
    b = int(input("enter number: "))
    l.append(b)
l2 = bubblesort(l)
b = int(input("enter element to search: "))
c = 1
if a > l2[(a - 1) // 2]:
    for i in range((a - 1) // 2, a):
        if l2[i] == b:
            print("element found at: ", i + 1, " position")
            c = 0
            break
else:
    for i in range((a - 1) // 2):
        if l2[i] == b:
            print("element found at: ", i + 1, " position")
            c = 0
            break
if c:
    print("ELEMENT NOT FOUND!!")
