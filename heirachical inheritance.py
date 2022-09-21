# heirachical inheritance

class Grand():
  def display_grand(self):
    print("this is class grand")
class Parent(Grand):
  def display_parent(self):
    print("this is parent class")
class Child(Grand):
  def display(self):
    print("this is child class")
obj = Child()
obj2 = Parent()
obj.display()
obj.display_grand()
obj2.display_parent()
obj2.display_grand()