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

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

import re 
txt ="The rain in Spain"
x= re.sub("\s","9",txt)
print(x)
