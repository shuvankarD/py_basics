# thisdict = {
#   "brand":"BMW",
#   "model":"mustang",
#   "year" :1955,
#    "year" :1902,
#   "colour" :['red','white','green']
# }
# thisdict.update({"year":2023})
# print(thisdict)
#
# band = {
# "pink floyd":"The who",
# "Metallica":"Iron Maiden",
# "Nirvana":"Beatles"
# }
# music= band.copy()
# print(music)

# child1={
# "Name":"thomas",
# "DOY":"1990"
# },
# child2={
#  "Name":"Greg",
#  "DOY": "1990"
# },
# child3={
#  "Name":"Rick",
#  "DOY": "1997"
# }

# Myfamily ={
# "child1" : child1,
# "child2" : child2,
# "child3" : child3
# }
# print(Myfamily)

# my_dict = {'name': 'John',
#  1: [2, 4, 3]}

# print(my_dict)

# my_dict = {'name': 'Jack', 'age': 26}

# print(my_dict.get('school'))

# my_dict ['age'] = 27
# my_dict ['Salary'] = 40000

# print(my_dict)

# squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# del squares


# original_marks = {'Physics':67, 'Maths':87}

# copied_marks = original_marks.copy()


# print('Original Marks:', original_marks)
# print('Copied Marks:', copied_marks)

# original = {1:'one', 2:'two'}
# new = original.copy()


# # removing all elements from the list

# original.clear()

# print('new: ', new)
# print('original: ', original)

# keys for the dictionary
# alphabets = {'a', 'b', 'c'}

# value for the dictionary
# number = {2,3}, {4,5}

# creates a dictionary with keys and values
# Hui = dict.fromkeys(alphabets)

# print(Hui)

# Output: {'a': 1, 'c': 1, 'b': 1}

# set of vowels
# keys = {'a', 'e', 'i', 'o', 'u' }

# # list of number
# value = [1,2]

# vowels = dict.fromkeys(keys, value)
# print(vowels)

# # updates the list value
# value.append(2)

# print(vowels)

# vowels keys
# keys = {'a', 'e', 'i', 'o', 'u' }
# value = [1]

# # creates dictionary using dictionary comprehension
# vowels ={ key : list(value) for key in keys } # dict.fromkeys(keys, value)  

# print(vowels)

# # updates the value list
# value.append(2)
# print(vowels)

# marks = {'Physics':67, 'Maths':87}

# print(marks.get("Maths"))
# person = {'name': 'Phill', 'age': 22}

# print('Name: ', person.get('name'))

# print('Age: ', person.get('age'))

# # value is not provided
# print('Salary: ', person.get('salary'))


# # value is provided
# print('Salary: ', person.get('salary', 0.0))

# print(person)

#person = {}

# Using get() results in None
# print('Salary: ', person.get('salary'))


# Using [] results in KeyError
# print(person['salary'])

# marks = {'Physics':67, 'Maths':87}

# print(marks.items())

# random sales dictionary
# sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

# items = sales.items()

# print('Original items:', items)

# delete an item from dictionary
# del(sales['apple'])

# print('Updated items:', items)

marks = { 'Physics': 67, 'Chemistry': 72, 'Math': 89 }

ipa=marks.pop('Chemistry')

print('Popped Marks:', ipa)