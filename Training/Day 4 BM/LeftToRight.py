def XoR(a):
    if a%4==1:
        return 1
    if a%4==2:
        return a+1
    if a%4==3:
        return 0
    if a%4==0:
        return a
l,r=map(int,input().split())
n=XoR(r)
b=XoR(l-1)
print(n^b)
