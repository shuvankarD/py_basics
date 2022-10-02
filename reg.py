# import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

# import re

# txt = "The rain in Spain"
# x = re.search("ai", txt)

# import re

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.string)

# import re

# txt = "The rain in Spain"
# x = re.findall("in", txt)
# print(x)

# import re

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print(x)

# import re
# txt = "The rain in Spain"
# x = re.split("\s",txt)
# print(x)

# import re

# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)

# import re 
# txt ="The rain in Spain"
# x= re.sub("\s","9",txt)
# print(x)

import re
txt = "The rain in Spain"
x = re.findall("[a-m]",txt)
print(x)

import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)

import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("hell.", txt)
print(x)

import re

txt = "hellllllllllo planet"

#Check if the string starts with 'hello':

x = re.findall("$ planet", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")



#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)

import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)

import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)

import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("Brazil|Django", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

