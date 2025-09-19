a = int(input("Enter a number: "))
a1 = 0
while a != 0:
    d = a % 10
    a1 += d
    a = a // 10
flag = 0
for i in range(2, a1):
    if a1 % i == 0:
        flag += 1
if flag == 0 and a1 > 1:
    print("Googly Number")
else:
    print("Not Googly Number")