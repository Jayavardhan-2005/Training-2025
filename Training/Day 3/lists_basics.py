# Merge 2 lists:
# l1=list(map(int,input().split()))
# l2=list(map(int,input().split()))
# l=l1+l2
# l.sort()
# print(l)
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# To swap first and last element of list
# l1=list(map(int,input().split()))
# l1[0],l1[-1] = l1[-1],l1[0]
# print(l1)
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# To remove duplicate elements in a list
# l=list(map(int,input().split()))
# l1 = []
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#Odd number of occurences in a list
# list1=[4,7,5,2,2,5,7,3,2,7,4]
# c=0
# list2=[]
# for i in range(len(list1)-1):
#     for j in range(i+1,len(list1)):
#         if list1[i]==list1[j]:
#             c+=1
#     if c%2==0:
#         if list1[i] not in list2:
#             list2.append(list1[i])
#     c=0
# print(list2)

#|||||||||||||||||||||||||||||||||||||||||
#Sum of minimum elements
# l=list(map(int,input().split()))
# l.sort
# print(sum(l[:3]))
#||||||||||||||||||||||||||||||||||||||||||||||||

#Odd ascending and descending using 2 lists
# l=list(map(int,input().split()))
# e=[]
# o=[]
# for i in l:
#     if i%2==0:
#         e.append(i)
#     if i%2==1:
#         o.append(i)
# e.sort()
# e.reverse()
# o.sort()
# results=e+o
# print(results)

# ||||||||||||||||||||||||||||||||||||||||||

#Using Single list
# l=list(map(int,input().split()))
# l1=[]
# for i in l:
#     if i%2==0:
#         l1.insert(0,i)
#     else:
#         l1.append(i)
# print(l1)