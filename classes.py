# class MyClass:
#   x = 5

# p1 =MyClass()
# print(p1.x)

# class beacontech:
#     def __init__(self, name, home, mobile):
#      self.name = name
#      self.home = home
#      self. mobile = mobile

#     def __str__(self):
#      return f"{self.name} {self.home} {self.mobile} "

# p1= beacontech("Sak","uttara",0O312000)
# # p2= beacontech("emrul","rampura",78687)

# print(p1)
#        # print(p2)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hui Hui , Enjoy your life"+ self.name) 

# p1 = Person("John",65)
# p1.myfunc()


# Python3 program to
# demonstrate instantiating
# a class
 
 
# class Dog:
#        attr1="hui"
#        attr2 ="kui"


#     # A sample method
#        def fun(self):
           
#         print("I'm a", self.attr1)
#         print("I'm a", self.attr2)
 
 
# # Driver code
# # Object instantiation
# Rodger = Dog()
 
# # Accessing class attributes
# # and method through objects
# #print(Rodger.attr1)
# #print(Rodger.attr2)
# Rodger.fun()


# Class for Dog
 
# class Dog:
#       animal ="dog"

#       def __init__(self, breed, colour):

#             self.breed ="breed"
#             self.colour = "colour"

# Rozer = Dog("German","ocean blue")
# Buzo  = Dog("Irish", "White")

# print("Rozer is a sweet" + Rozer.animal)
# print("Breed :",Rozer.breed)
# print("Colour :", Rozer.colour)

# print("\n")

# print("Buzo is a cute" + Buzo.animal)
# print("Breed :",Rozer.breed)
# print("Colour :", Rozer.colour)
  
  
# Discuss

# A class is a user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by their class) for modifying their state.

# To understand the need for creating a class in Python let’s consider an example, let’s say you wanted to track the number of dogs that may have different attributes like breed, and age. If a list is used, the first element could be the dog’s breed while the second element could represent its age. Let’s suppose there are 100 different dogs, then how would you know which element is supposed to be which? What if you wanted to add other properties to these dogs? This lacks organization and it’s the exact need for classes. 

# Syntax: Class Definition 

# class ClassName:
#     # Statement
# Syntax: Object Definition


# obj = ClassName()
# print(obj.atrr)
# Class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object.

# Some points on Python class:  

# Classes are created by keyword class.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute
# Defining a class 
# # Python3 program to
# # demonstrate defining
# # a class


# class Dog:
#     pass


# Example:

# python declaring an object

# Declaring an object

# # Python3 program to
# # demonstrate instantiating
# # a class
 
 
# class Dog:
 
#     # A simple class
#     # attribute
#     attr1 = "mammal"
#     attr2 = "dog"
 
#     # A sample method
#     def fun(self):
#         print("I'm a", self.attr1)
#         print("I'm a", self.attr2)
 
 
# # Driver code
# # Object instantiation
# Rodger = Dog()
 
# # Accessing class attributes
# # and method through objects
# print(Rodger.attr1)




# # Sample class with init method
# class Person:
 
#     # init method or constructor
#     def __init__(self, name):
#         self.name = name
 
#     # Sample Method
#     def say_hi(self):
#         print('Hello, my name is', self.name)
 
 
# p = Person('Nikhil')
# p.say_hi()
# Output: 

# Hello, my name is Nikhil
# Class and Instance Variables
# Instance variables are for data, unique to each instance and class variables are for attributes and methods shared by all instances of the class. Instance variables are variables whose value is assigned inside a constructor or method with self whereas class variables are variables whose value is assigned in the class.

# Defining instance variables using a constructor. 


# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.
 
# Class for Dog
 
 
# class Dog:
 
#     # Class Variable
#     animal = 'dog'
 
#     # The init method or constructor
#     def __init__(self, breed, color):
 
#         # Instance Variable
#         self.breed = breed
#         self.color = color
 
 
# # Objects of Dog class
# Rodger = Dog("Pug", "brown")
# Buzo = Dog("Bulldog", "black")
 
# print('Rodger details:')
# print('Rodger is a', Rodger.animal)
# print('Breed: ', Rodger.breed)
# print('Color: ', Rodger.color)
 
# print('\nBuzo details:')
# print('Buzo is a', Buzo.animal)
# print('Breed: ', Buzo.breed)
# print('Color: ', Buzo.color)
 
# Class variables can be accessed using class
# name also
# print("\nAccessing class variable using class name")
# print(Dog.animal)
# Output
# Rodger details:
# Rodger is a dog
# Breed:  Pug
# Color:  brown

# Buzo details:
# Buzo is a dog
# Breed:  Bulldog
# Color:  black

# Accessing class variable using class name
# dog
# Defining instance variables using the normal method.


# Python3 program to show that we can create
# instance variables inside methods
 
# Class for Dog
 
 
class Dog:
 
    # Class Variable
    animal = 'dog'
 
    # The init method or constructor
    def __init__(self, breed):
 
        # Instance Variable
        self.breed = breed
 
    # Adds an instance variable
    def setColor(self, color):
        self.color = color
 
    # Retrieves instance variable
    def getColor(self):
        return self.color
 
 
# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())
print(Rodger.breed)


        


