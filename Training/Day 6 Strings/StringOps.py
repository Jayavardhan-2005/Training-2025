# To check the count of digits and alphabets
a=input()
count_al=0
count_num=0
for i in a:
    if i.isalpha():
        count_al+=1
    if i.isnumeric():
        count_num+=1
print(count_num,count_al)