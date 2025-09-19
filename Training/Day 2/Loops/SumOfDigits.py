# To find the sum of digits in a number
a=int(input())
sum=0
while a!=0:
    d=a%10
    sum=sum+d
    a=a//10
print(sum)
