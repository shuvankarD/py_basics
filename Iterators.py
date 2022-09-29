# mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

class MyNumbers:
  def __iter__(self):
    self.a = 2
    return self

  def __next__(y):
    if y.a <= 20: 
     x = y.a
     y.a += 2
     return x
    else:
      raise StopIteration

# myclass = MyNumbers()
myiter = iter(MyNumbers())

for x in myiter: 
      print(x) 