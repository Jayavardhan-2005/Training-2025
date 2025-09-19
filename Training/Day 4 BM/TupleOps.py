#To remove a element from a tuple (Using list)
# a=tuple(map(int,input().split()))
# i=int(input())
# lst=list(a)
# for x in range(len(lst)):
#     if x==i:
#         lst.remove(x)
# print(tuple(lst))

# Remove element at given index from tuple without using list
a = tuple(map(int, input().split()))
i = int(input())
t = a[:i] + a[i+1:]
print(t)
