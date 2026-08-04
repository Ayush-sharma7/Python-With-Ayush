def rev(x):
    s=0
    while(x):
        s=s*10+x%10
        x//=10
    return s
#main
a=int(input("enter number: "))
sq=lambda x:x**2
if(sq(a)==rev(sq(rev(a)))):
    print("given number is an adam number")
else:
    print("not a adam number")