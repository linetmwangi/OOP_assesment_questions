class Animal:
    def sound(self):
        return "some generic animal sound"

class Cat(Animal):
  def __init__(self,name):
      self.name = name

  def sound(self):
      return "meows"

class Dog(Animal):
    def sound(self):
        return "barks"

cat1 = Cat("cat")
print(cat1.sound())
dog1 = Dog()
print(dog1.sound())
