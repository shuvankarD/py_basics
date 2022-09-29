# def my_function(*fname):
#     print( "Allocated people are"+ fname[1])
# my_function("Robert","Zimenski","Hanks","Pellegrini")
#
# def my_function(child1, Child2, Child3):
#      print("The Youngest Child is "+ Child3)
# my_function(child1 ="Emil",Child2 ="Thobas",Child3 ="Martin")

# def my_function(**kid):
#   print("His last name is " + kid["lname"])
#
# my_function(fname = "Tobias", lname = "Refsnes")

# def my_function(country = "Norway"):
#   print("I am from " + country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):
#     for x in food:
#      print(x)

# food=["apple","orange","mango"]
# my_function(food)

# def my_function(x):
#     return 5*x

# print(my_function(3))
# print(my_function(5))


# def recursion(k):
#   if (k>0):
#     result = k+ recursion(k-1)
#     print (result)
#   else:
#     result =0
#     return result
# recursion(6)
# def student(firstname, lastname):
#     print(firstname, lastname)
 
 
# # Keyword arguments
# student(firstname='Geeks', lastname='Practice')
# student(lastname='Practice', firstname='Geeks')



# def myFun(**kwargs):
#     for key,value in kwargs.items():
#         print("%s == %s" % (key,value))
 
 
# # # Driver code
#  myFun(first='Geeks', mid='for', last='Geeks')


# def myFun(x, y=50):
#     print("x",x)
#     print("y", y)
 
 
# # Driver code (We call myFun() with only
# # argument)
# myFun(10)

# def myfunc(*argv):
#     for argv in argv:
#         print(argv)

# myfunc("Hello","Hi") 


# A simple Python function to check
# whether x is even or odd
 
 
# def func(x):

#     if( x % 2 == 0 ):
#         print("even")
#     else:
#         print("odd")

# func(2)
# func(3)

# def square_value(num):
#     """This function returns the square
#     value of the entered number"""
#     return num**2

# print(square_value(-4))
# print(square_value(-5))

# Here x is a new reference to same list lst

# def myFun(x):
#    x[1:2] = [45,70]
   
# x = [10, 11, 12, 13, 14, 15]
# (myFun(x))
# print(x)
 
# Driver Code (Note that lst is modified
# after function call.
 

# def function(int):
#   int=+100
#   print("Inside function call ",int)
  
# int=200
# print("Before function call ",int)
# function(int)
# print("After function call ",int)

# def function(int):
#   int=+100
#   print("Inside function call ",int)

# int=200
# print("Before function call ",int)
# function(int)
# print("After function call ",int)





# def function(int):
#    int.append('B')
#    print("Inside function call",int)
     
# int=['A']
# print("Before function call",int)
# function(int)

# print("After function call",int)


def myFun(x):
 
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
  

#   x = [20, 30, 40]
  
    
 
# # Driver Code (Note that lst is not modified
# # after function call.
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)

#  def myFun(x):
 
#     # After below line link of x with previous
#     # object gets broken. A new object is assigned
#     # to x.
#     x = 20
 
 
# # Driver Code (Note that lst is not modified
# # after function call.
# x = 10
# myFun(x)
# print(x)

