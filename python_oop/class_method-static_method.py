
# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Take Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself
# Static Methods:
# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class
# -----------------------------------------------------------

class Iterator():
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        return self.count

class User:

    # class attribute
    users_count = 0
    #initialize itertator
    iterator = Iterator()
    # Class-level list to store instances
    instances = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.users_count += 1   
        #add instance to the class-level list
        User.instances.append(self)

    # class method
    @classmethod
    def getUsersCount(cls):
            count = next(cls.iterator)
            print(f"{count}-we have {cls.users_count} users")

    #static method
    def sayHello(self):
        return "this message from static method, it's general: for all users we don't need any infos"

User.getUsersCount()

user1 = User('Ahmed',14)
user2 = User('Yasser',19)

User.getUsersCount()

print('#'*50)

for user in User.instances:
     print(f'Hello {user.name}, {user.sayHello()} ')


