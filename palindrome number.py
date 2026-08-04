#palindrome number or not?
a=int(input("enter number: "))
t=a
s=0
while(a):
    s=s*10+a%10
    a//=10
if(s==t):
    print(t," is a palindrome number!")
else:
    print(t," is not a palindrome number!")
