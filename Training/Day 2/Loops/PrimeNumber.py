# To check whether the number is a prime number or not
# a=int(input())
# flag = 0
# for i in range(2,a):
#     if a%i==0:
#         flag+=1
# if flag==0:
#     print("Prime")
# else:
#     print("Not Prime")

# Prime numbers in a range from a to b
def isprime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
l = int(input())
r = int(input())
c = 0
for i in range(l,r+1):
    if isprime(i):
        c+=1
print(c)