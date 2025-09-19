# a=int(input())
# if a%4==0:
#     print(1)
# elif a%4==1:
#     print(a+1)
# elif a%4==2:
#     print(0)
# elif a%4==3:
#     print(a)

# function method
def XoR(a):
    if a%4==1:
        return 1
    if a%4==2:
        return a+1
    if a%4==3:
        return 0
    if a%4==0:
        return a
a=int(input())
print(XoR(a))