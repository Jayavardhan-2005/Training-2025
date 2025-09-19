# Greatest Of Three Numbers
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print("A is greatest")

elif b>c:
    print("B is greatest")

else:
    print("C is greatest")
'''
a,b,c=5,10,11-->
map syntax : map(datatype or variable)
example : a,b,c = map (int , input().split())-->for input of 3 or more elements statically
a,b,c = map (int , input().split(","))--> for input of three elements in a single line and 
     input is taken with spaces (dynamically)
'''