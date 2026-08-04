
a,b=map(int,input("input marks and family income: ").split())
if(a>=75 and b<=250000):
    print("eligible")
else:
    print("not eligible")

u=int(input("enter units: "))
b=0
if(u<=100):
    b=u*2
if(u<=200):
    u-=100
    b+=u*3
if(u>200):
    b-=200
    b+=u*5
print(b)

a,b,c=map(int,input("enter 3 sides of triangle: ").split())
if(a+b>c):
    print("triangle is valid!")
else:
    print("invalid triangle!")

a=input("enter character: ")
if(a>="A" and a<="Z"):
    print("uppercase")
elif(a>="a" and a<="z"):
    print("lowercase")
elif(a>="1" and a<="9"):
    print("it is digit")
else:
    print("its special character")

s=float(input("enter salary: "))
y=int(input("enter years: "))
b=0
if(y>=10):
    b=s+s*0.1
elif(y>=5):
    b=s+s*0.07
else:
    b=s+s*0.05
print(b)

a,w=map(int,input("enter balance and withdrawal amount: ").split())
if(w%100==0 and w<=a):
    print("withdrawal successful")
else:
    print("unsuccessful attempt")

a=int(input("enter marks: "))
if(marks>=40):
    print("pass")
elif(marks>=35 and marks<40):
    print("pass with grace")
else:
    print("failed")

a,b,c=map(int,input("enter three numbers: ").split())
s=a+b+c
m=max(a,b,c)
m2=min(a,b,c)
d=s-m-m2
print(d)

a=int(input("enter value: "))
if(a<25):
    print("high premium")
elif(a>=25 and a<=50):
    print("medium premium")
else:
    print("low premium")

u,p=map(str,input("enter username and password: ").split())
if(u=="admin" and p=="python123"):
    print("login successful")
else:
    print("unsuccessful")   

a,b=map(int,input("enter weekly money and no. of weeks: ").split())
print(a*b)

c,f=map(int,input("enter no. of candies and total number of friends: ").split())
if(c%f):
    print("each friend will get ",c//f," candies and ",c%f," leftover")
else:
    print("each friend will get: ",c//f," candies")

e,f=map(int,input("enter efficiency and total amount of fuel: ").split())
print(e*f)

m,t=map(int,input("enter movie duration and total time: ").split())
if(t%m):
    print("you can watch ",t//m," movies and time left after the marathon ",t%m," minutes")

a,b,c,d=map(int,input("enter accomodation cost, daily food cost, daily entertainment cost and total number of days: ").split())
print((a+b+c)*d)

a,b,c=map(int,input("enter total flour, total cookies by the original recipe and expected cookies: ").split())
print(a/b*c," required")






                    
