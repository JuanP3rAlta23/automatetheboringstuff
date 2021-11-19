# The definition of the hello() function in this program has a parameter called name. 
# Parameters are variables that contain arguments. 
# When a function is called with arguments, the arguments are stored in the parameters.
def hello(name):
   print('Hello, ' + name)
#The first time the hello() function is called, it is passed the argument 'Juan'.
#The program execution enters the function, and the parameter name is automatically set to 'Juan', 
# which is what gets printed by the print() statement 
hello('Juan')
hello('Rita')