a = int(input())
b = int(input())
c = int(input())
d = int(input())
l = []
f = []
for i in range(12):
    for j in range(12):
        for k in range(12):
            if i <= a and j <= b and k <= c:
                l = [i, j, k]
                if sum(l) != d:
                    f.append(l)
print(f)
