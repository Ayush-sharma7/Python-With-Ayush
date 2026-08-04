# two sum problem
l = list(map(int, input("enter values: ").split()))
t = int(input("enter number: "))
l2 = []
for i in range(0, len(l)):
    for j in range(0, len(l)):
        l3 = []
        if i != j:
            if l[i] + l[j] == t:
                l3.append(i)
                l3.append(j)
                l2.append(l3)
                break
print(l2)
