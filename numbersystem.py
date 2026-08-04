'''a=int(input("enter number: "))
if(a==0):
    print("zero")
elif(a==1):
    print("one")
elif(a==2):
    print("two")
elif(a==3):
    print("three")
elif(a==4):
    print("four")
elif(a==5):
    print("five")
elif(a==6):
    print("six")
elif(a==7):
    print("seven")
elif(a==8):
    print("eight")
elif(a==9):
    print("nine")
else:
    print("invalid")

a=int(input("enter number: "))
l=['zero',"one",'two','three','four','five','six','seven','eight','nine']
l2=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen']
l3=['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty','hundred']
if(a<10):
    print(l[a])
elif(a<20 and a>=10):
    print(l2[a-10])
elif(a>=20 and a<100 and a%10):
    s=(a//10)-2
    r=a%10
    print(l3[s]+l[r])
elif(a%10==0):
    print(l3[(a//10)-2])

u=int(input("enter units: "))
b=0
if(u>200):
    b=(u-200)*10
    u=u-(u-200)
if(u>100 and u<=200):
    b+=(u-100)*7
    u=u-(u-100)
if(u<=100):
    b+=u*5
print(b)

a,b,c,d=map(bool,input(''enter if
fees paid,
special permission or assignment,
not banned: '').split())
if(a and (b or c) and d):
    print("allowed")
else:
    print("not allowed")

a=int(input("enter number: "))
for i in range(1,a+1):
    print(i,end=" ")

a=int(input("enter number: "))
s=(a*(a+1))/2
print(s)'''

a=int(input("enter range: "))
for i in range(1,a+1,2):
    print(i)

a=int(input("enter range: "))
for i in range(1,10):
    print(i,'x',a,'=',i*a)

a=input("enter number: ").strip()
print(len(a))

a=input("enter number: ").strip()
print(a[::-1])

a=int(input("enter number: "))
s=1
for i in range(1,a+1):
    s*=i
print(s)

a=input("enter string: ")
for i in a:
    print(i)

a=int(input("enter number: "))
s=0
while(a):
    s=s*10+a%10
    a//=10
print(s)

a=input("enter string: ")
c=0
for i in a:
    if(i in "aeiou"):
        c+=1
print(c)

