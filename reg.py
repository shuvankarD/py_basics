import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.search("ai", txt)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)