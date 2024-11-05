class Animal:
    def eat(self):
        print("The animal is eating.")

    def sleep(self):
        print("The animal is sleeping.")


class Dog(Animal):
    def bark(self):
        print("The dog is barking.")



dog = Dog()

dog.eat()
dog.sleep()
dog.bark()