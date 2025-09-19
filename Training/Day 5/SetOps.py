# For union: use or (or) |
# For intersection : use and (or) &
# SET BUILT-IN FUNCTIONS

# sum():
# Returns the sum of all elements in the set.

# max():
# Return the largest item in the set.
# s = (1,2,3,4,5) print(sum(s))
# 15
# s = (1,2,3,4,5) print(max(s))
# 5

# min():
# Return the smallest item in the set.
# s = (1,2,3,4,5) print(min(s))
# 1

# len():e
# Return the length (the number of items) in the set.
# s = (1,2,3,4,5) print(len(s))
# 5
res={s for s in [1,2,3] if s%2}
print(res)