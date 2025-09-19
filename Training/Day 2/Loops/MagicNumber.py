a = int(input())
temp = a
while a > 9:
    a1 = 0
    while temp != 0:
        d = temp % 10
        a1 = a1 + d
        temp = temp // 10
    a = a1  
    temp = a 
if a == 1:
    print("Magic Number")
else:
    print("Not a Magic Number")
