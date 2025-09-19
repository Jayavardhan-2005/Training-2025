# To capitalize all the words in a string(without .title()):
o_str = input()
n_list = list(o_str)
for i in range(len(n_list)):
    if i == 0 or n_list[i-1] == " ":
        if n_list[i].isalpha():
            n_list[i] = n_list[i].upper()
n_str = "".join(n_list)
print(n_str)

# With .title():
# a = input()
# print(a.title())