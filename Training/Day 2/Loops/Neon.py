"""
Definition:
A number is called a Neon Number if the sum of the digits of its square is equal to the number itself.

Example 1:

Take 9.

Square: 9^2 = 81

Sum of digits of 81: 8 + 1 = 9
Since the sum (9) is equal to the original number (9), 9 is a Neon Number.
"""
a = int(input())
sq = a * a
s = 0
while sq != 0:
    d = sq % 10
    s = s + d
    sq = sq // 10

if s == a:
    print(a, "is a Neon Number")
else:
    print(a, "is NOT a Neon Number")
