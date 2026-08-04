import pickle

file = open("Stud.dat", "wb")
n = int(input("Enter number of records"))
d = {}
for i in range(1, n + 1):
    d["rno"] = int(input("Enter roll no"))
    d["name"] = input("Enter name")
    d["marks"] = float(input("Enter marks"))
    pickle.dump(d, file)
file.close()
try:
    file = open("Stud.dat", "rb")
    while True:
        d = pickle.load(file)
        print(d)
except:
    print("all records printed successfully")
    file.close()
