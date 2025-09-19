a=int(input())
if a<=1:
    print("not a composite number")
temp=a
c=0
for i in range(1,temp+1):
    if temp%i==0:
        c+=1
if c>2:
    print("Is a composite number")
else:
    print("Not a composite number")