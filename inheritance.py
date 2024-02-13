# This is the parent class/Base class/Super class
class animal:
    def sound(self):
        print("Animal is speaking")
# Child class/Sub class/Derived class

class dog(animal):
    def bark(self):
        print("Dog is barking")


class cat(animal):
    def meow(self):
        print("Cat is meowing")


a = animal()
d = dog()
d.sound()
c = cat()
c.meow()