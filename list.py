
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# newlist = ['hello' for x in fruits]
#
# print(newlist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)
# def myfunc(m):
#     return abs(n - 50)
#
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key= myfunc)
# print(thislist)

# def add(a,b):
#     return a+b
# def is_true(a):
#     return bool(a)
# res =add(4,5)
# print("print  {}".format(res))
# res =is_true(2<5)
# print("\n Hui Hui {}".format(res))

# def add(a, b):
#
#     # returning sum of a and b
#     return a + b
#
# def is_true(a):
#
#     # returning boolean of a
#     return bool(a)
#
# # calling function
# res = add(2, 3)
# print("Result of add function is {}".format(res))
#
# res = is_true(2<5)
# print("\nResult of is_true function is {}".format(res))

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)
#
# list1 = ['a','b','c']
# list2 = [1,2,3]
#
# for x in list1:
#     list2.append(x)
#     print(list2)
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

# my_list = ["mouse", [8, 4, 6], ['a']]
# print(my_list)

# my_list = ['p', 'r', 'o', 'b', 'e']

# # first item
# print(my_list[0])  # p

# # third item
# print(my_list[2])  # o

# # fifth item
# print(my_list[4])  # e

# Nested List
# n_list = ["Happy", [2, 0, 1, 5],["Shuv","nik"]]

# # Nested indexing
# print(n_list[2][1])

# print(n_list[1][3])

# my_list = ['p','r','o','b','e']

# # last item
# print(my_list[-1])

# # fifth last item
# print(my_list[-5])

# my_list = ['p','r','o','g','r','a','m','i','z']

# print(my_list[1:3])
# print(my_list[:-3])
# print(my_list[:])

odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  

print(odd) 