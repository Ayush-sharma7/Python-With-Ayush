a = int(input())
l1 = []
for i in range(a):
    l = list(map(str, input().split()))
    l1.append(l)
t = input()
for i in range(a):
    if l1[i][0] == t:
        p = (float(l1[i][1]) + float(l1[i][2]) + float(l1[i][3])) / 3
        print(format(p, ".2f"))
