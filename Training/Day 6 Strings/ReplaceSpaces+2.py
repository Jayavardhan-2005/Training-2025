# To replace spaces with "-"(without replace):
# a = input()
# result = ""
# for i in a:
#     if i == " ":
#         result += "-"
#     else:
#         result += i
# print(result)

# With Replace:
# a=input()
# a=a.replace(" " , "-")
# print(a)

# With ispace() :
a=input()
b=""
for i in a:
    if i.isspace():
        i+="-"
    else:
        b+=i
print(b)