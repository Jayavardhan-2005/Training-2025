# a=int(input())
# sum=0
# for i in range(1,a):
#     if a%i==0:
#         sum+=i
# if a==sum:
#     print("Is a perfect number")
# else:
#     print("Is not a perfect number")

#Strong Number:
# a=int(input())
# a1=a
# sum=0
# while a>0:
#     d=a%10
#     fact=1
#     for i in range(1,d+1):
#         fact*=i
#     sum+=fact
#     a=a//10
# if sum==a1:
#     print("Strong number")
# else:
#     print("Not a strong number")

#SpyNumber:
a = int(input())
sum = 0
m=1
while a>0:
    d=a%10
    sum+=d
    m*=d
    a//=10
if sum==m:
    print("Spy number")
else:
    print("Not a spy number")