
# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------

class Member:
  def __init__(self, name):
    self.__name = name  # Private

  def say_hello(self):
    return f"Hello {self.__name}"

  # because of the attribute name is private, we create a getter to get the name  of the object member created
  def get_name(self):  # Getter
    return self.__name

  # other method of getter using @property
  @property
  def name(self): # Getter
    try:
      print("Hello {} from getter that use property decorator".format(self.__name))
      return self.__name
    except AttributeError:
      print("The user not found, maybe was deleted")

  def set_name(self, new_name): #setter
    self.__name = new_name

  # other method of setter using @attribute_name.setter
  @name.setter
  def name(self, new_name): #setter
    print("Hello {} from setter, your new name is {}".format(self.__name,new_name))
    self.__name = new_name

  @name.deleter
  def name(self): #deleter
    print(f'{self.__name} wad deleted')
    del self.__name 

one = Member("Ahmed")

# this method to get a private (or protected) attribute is not professional
one._Member__name = "Omar"
member = Member("Yasser")

print(one._Member__name)

# this is professional
print(one.get_name())
one.set_name('Yasser')
print(one.get_name())

#this is more professional in python
print(member.name) #Yasser # Accessing the property directly, not calling it as a function
member.name = "Karim"
print(member.name) #Karim
del member.name
print(member.name)