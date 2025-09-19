# To check if the given string is a palindrome or not using two pointer:
a = input()
i = 0
j = len(a) - 1
while i < j:
    if a[i] != a[j]:
        print("Not a Palindrome")
        break
    i += 1
    j -= 1
else:
    print("Palindrome")

