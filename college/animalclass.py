class animal:
    def sound(self):
        print("Animal make sounds")
class  Dog(animal):
    def bark(self):
        print("Dog barks")

d=Dog()
a=animal()
d.sound()
a.sound()
d.bark()