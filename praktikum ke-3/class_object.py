class MyClass:
  x = 5
print (MyClass) 

class MyClass:
  x = 20

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(p1)

class IniKelas:
  x = "kembali pulang"

p1 = IniKelas()
p2 = IniKelas()
p3 = IniKelas()

print(p1.x)
print(p2.x)
print(p3.x)

class Person:
  pass