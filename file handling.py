import csv

f = open("student.csv", "a+")
w = csv.writer(f)
l = []
l2 = []
for i in range(5):
    a = input("enter name:")
    b = int(input("enter marks:"))
    l = [a, b]
    l2.append(l)
w.writerows(l2)
f.close()
