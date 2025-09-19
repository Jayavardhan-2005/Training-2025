# You are given a string str. Your task is to find the number of checks that is not satisfied by the string str by checking the validation of the string str 
# if it's a strong password or not. A password is a strong password only if:
# It contains at least 6 characters and at most 22 characters.
# It must contain at least one uppercase character.
# It must contain at least one lowercase character.
# It must contain at least two special characters (@, I, &, ^,%,",#).
# It must contain at least one numeric value.
# It must not contain any two same consecutive character.
# Input Format:
# The input consists of a single line: The first line contains a string str. 
# The input will be read from the STDIN by the candidate.
# Output Format:
# Print the number that represents the number of checks that is not satisfied by the str.
# The output will be matched to the candidate's output printed on the STDOUT.

a = input()
b = 0
spe_char = '@&^%#,'
num_char = '0123456789'
s_count = 0
n_count = 0
if len(a) < 6 or len(a) > 22:
    b += 1
if a.lower() == a:
    b += 1
if a.upper() == a:
    b += 1
for i in a:
    if i in spe_char:
        s_count += 1
    if i in num_char:
        n_count += 1
if s_count < 2:
    b += 1
if n_count < 1:
    b += 1
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        b += 1
        break
print(b)