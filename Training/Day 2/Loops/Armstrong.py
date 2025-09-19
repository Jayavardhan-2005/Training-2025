a = int(input())
a1 = a
count = 0
a2 = a
while a2 != 0:
    count += 1
    a2 //= 10
sum = 0
while a2 != 0:
    d = a2 % 10
    sum += d ** count
    temp //= 10
if sum == a1:
    print("Armstrong number")
else:
    print("Not Armstrong number")