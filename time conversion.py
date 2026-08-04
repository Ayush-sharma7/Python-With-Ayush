t = input().split(":")
if t[0] == "12" and t[2][2:] == "AM":
    print("00:" + t[1] + ":" + t[2][:2])
elif t[0] == "12" and t[2][2:] == "PM":
    print(t[0] + ":" + t[1] + ":" + t[2][:2])
elif t[2][2:] == "PM" and int(t[0]) >= 1:
    t = str(int(t[0]) + 12) + ":" + t[1] + ":" + t[2][:2]
    print(t)
else:
    print(t[0] + ":" + t[1] + ":" + t[2][:2])
