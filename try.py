try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

#   x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# x ="Hello"
# if not type(x) is int:
#     raise TypeError ("Pls Int only")


try:
  print(x)
# except NameError:

#print("Variable is not defined")
except :
  print("Something else is went wrong") 