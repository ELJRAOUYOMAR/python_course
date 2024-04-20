#Recursion is a programming technique where a function calls itself in order to solve a problem. 

def add_numbers(number):
    if number == 0:
        return 0;   
    else:
        return number + add_numbers(number-1)
    
number = int(input("Tap a number"))
print("final number is {}".format(add_numbers(number)))