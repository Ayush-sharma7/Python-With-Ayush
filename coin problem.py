#COIN PROBLEM
n,a=map(int,input().split())
l=list(map(int,input().split()))
c=0
l.sort(reverse=True)
for i in l:
    while(a-i>=0):
        a-=i
        c+=1
if(a>0 or c>n):
    print(-1)
else:
    print(c)
