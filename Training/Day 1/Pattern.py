a = int(input())
for i in range(a):
    for j in range (a):
        print("*" , end = " ")
    print()
#READ ME FOR INFO:
'''
for i in range(1,rows+1):
    print("*" * i)-->for left angled triangle

for i in range(1,row+1):
    print(" " * (rows-i) + "*" * i)--> for right angled triangle

for i in range(1,rows+1):
    print(" " * (rows-i) + "*" *(2*i-1))--> for central triangle

for i in range(rows,0,-1):
    print("*" * i)--> for inverted left

for i in range(rows,0,-1):
    print(" " * (rows-i) + "*" * i)--> for inverted right

for i in range(rows,0,-1):
    print(" " * (rows-i) + "*" *(2*i-1))--> for inverted central

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
-->Square Snake Pattern
rows=int(input())
num = 1
for i in range(1,rows+1):
    line=[]
    for j in range(1, rows+1):
        line.append(str(num))
        num+=1

    if i%2==0 :
        line.reverse()

    print(" ".join(line))
OUTPUT:
1 2 3 4
8 7 6 5
9 10 11 12
16 15 14 13
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
'''