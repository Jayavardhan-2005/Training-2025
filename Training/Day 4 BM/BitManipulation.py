#Even and Odd Number without using modulus
# n=int(input())
# if n&1==0:
#     print("Even")
# else:
#     print("Odd")

#Number swap without temnporary variables:
a,b=map(int,input().split())
a=a^b
b=b^a
a=a^b
print(a)
print(b)