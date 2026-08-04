l = []
a = int(input("enter no. of cities:"))
for i in range(0, a):
    b = input("enter city name:")
    l.append(b)
d = {}
for i in range(0, len(l)):
    d[l[i]] = i + 1
print(d)
