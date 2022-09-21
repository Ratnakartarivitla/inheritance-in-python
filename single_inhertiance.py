#inheritance
# the proces of aacquiring properties from parent call to the base calss
# single  inheritance
class Parent():
  def display_parent(self):
    print("this is parent class")
class Child(Parent):
  def display(self):
    print("this is child class")
obj = Child()
obj.display() 
obj.display_parent()