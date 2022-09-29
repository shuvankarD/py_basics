# thisset = {"apple", "banana", "cherry", "apple"}
#
# print(len(thisset))
#
# set1 = {"abc", 34, True, 40, "male"}
# print(set1)

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#   print(x)

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)
