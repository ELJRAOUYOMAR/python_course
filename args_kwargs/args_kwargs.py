# https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/


# *args is used to send a non-keyworded variable length argument list to the function. 
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    if argv is not None:
        for arg in argv:
            print("another arg through *argv :", arg)

test_var_args('Yasser','python','eggs','test')

# **kwargs allows you to pass keyworded variable length of arguments to a function. You should use **kwargs if you want to handle named arguments in a function
def greet_me(**kwargs):
    # not crucial
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" %(key,value))

print("#"*40)
greet_me(name="Yasser",age=20)

