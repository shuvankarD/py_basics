# x = lambda  a : a+ 10
# print(x(5))

# def myfunc(a):
#   return lambda a : a * 10

# print(myfunc(11))

# x = lambda a,b : a *b
# print(x(4,6))

# x = lambda a,b,c : a + b + c
# print(x(2,4,6))

# def myfunc(n):
#   return lambda a : a * n

def myfunc(n):
  return lambda a: a * n
result1 = myfunc(3)
result2 = myfunc(5)
print(result1(11))
print(result2(11))