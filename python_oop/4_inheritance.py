"""
In Python, inheritance refers to the capability of a class to derive properties and behaviors 
from another class. The derived class (subclass) can access and extend the attributes and methods
of the base class (superclass), allowing for code reuse and facilitating the creation of hierarchical
relationships between classes.
"""
class A: #direct super class from B, indiract super class for C 
    age: int

    def info(self):
        self.age = 10
        print("age= {}".format(self.age))

class B(A):  #direct super class for C, sub class for A
    def info2(self):
        # print("age= {}".format(self.age))
        super().info()

class C(B):  #sub class for A and B
    def info2(self):
        print("age= {}".format(self.age))


instance_from_B = B()
instance_from_B.info2()

instance_from_C = C()
instance_from_C.info2()
