# To find the length of the longest word in a string:
a= input()
l= max(len(word) for word in a.split())
print(l)