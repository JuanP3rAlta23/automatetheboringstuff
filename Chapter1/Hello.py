# This program says hello and asks for your name

print('Hello world!')

print ('What is your name?') # ask for your name
myName = input()
print('Its is good to meet yo,' + myName)
print('the length of your name is:')
print(len(myName))

print('What is your age?') #ask for your age
myAge = input()
print ('You will be ' + str(int(myAge)+ 1) + 'in a year.')
