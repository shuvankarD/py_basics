# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()

# class teacher:
        
#     def __init__(self, firstname, lastname):

#             self.firstname =firstname
#             self.lastname = lastname

#     def name(self):
#         print(self.firstname,self.lastname)
                   


# class Student(teacher):
#     pass
    

# KK = Student("Shuvankar","Dash")   
# KK.name()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#     self.graduationyear1 = 2019
#     self.graduationyear2 =2020

# x = Student("Mike", "Olsen")
# y = Student("Rubayet","Saikat")


# x.printname() 
# print(x.graduationyear1)
# y.printname()
# print(y.graduationyear2)




     
# class Student:
#     # Class variable
#       school_name = 'ABC School'

#     # constructor
#       def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no

#     # Instance method
#       def show(self):
#         print(self.name, self.roll_no, Student.school_name)

# # create Object
# s1 = Student('Emma', 10)
# print('Before')
# s1.show()

# # Modify class variable
# s1.school_name = 'XYZ School'
# print('After')
# s1.show()

# class Course:
#     # class variable
#     course = "Python"

# class Student(Course):

#     def __init__(self, name):
#         self.name = name

#     def show_student(self):
#         # Accessing class variable of parent class
#         print('Before')
#         print("Student name:", self.name, "Course Name:", self.course)
#         # changing class variable value of base class
#         print('Now')
#         Student.course = "Machine Learning"
#         print("Student name:", self.name, "Course Name:", self.course)

# # creating object of Student class
# stud = Student("Emma")
# stud.show_student()

class Course:
    # class variable
    course = "Python"

class Student(Course):
    # class variable
    course = "SQL"

    def __init__(self, name):
        self.name = name

    def show_student(self):
        # Accessing class variable
        print('Before')
        print("Student name:", self.name, "Course Name:", Student.course)
        # changing class variable's value
        print('Now')
        Student.course = "Machine Learning"
        print("Student name:", self.name, "Course Name:", Student.course)

# creating object of Student class
stud = Student("Emma")
stud.show_student()

# parent class course name
print('Parent Class Course Name:', Course.course)


        




    
