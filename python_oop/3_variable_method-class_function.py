'''
*Class Variable:

-A variable that is shared among all instances of a class.
-Defined within the class but outside of any class methods.
-Accessed using the class name or instance name.
*Instance Variable:

-A variable that is unique to each instance of a class.
-Defined within the __init__ method or any other instance method.
-Accessed using the instance name.
*Class Method:

-A method that is bound to the class rather than its instances.
-Defined using the @classmethod decorator above the method.
-Typically used to modify or access class variables, or perform operations that are not specific to any instance.
'''

class Human:
    # class method
    @classmethod
    def info(cls):
        print("Hello from class method")

    def anything(self,any):
        print(any)

# call the method (directoly form the class, not the instance)
Human.info()        

print("*"*30)

anything_object = Human()
# we can call the instance method directly from the class
Human.anything(anything_object,"Hello from instance method")  # equal two anything_object.anything("Hello from instance method")