# multiple inheritance

class Grand():
  def display_grand(self):
    print("this is class grand")
class Parent():
  def display_parent(self):
    print("this is parent class")
class Child(Parent,Grand):
  def display(self):
    print("this is child class")
obj = Child()
obj.display() 
obj.display_parent()
obj.display_grand()