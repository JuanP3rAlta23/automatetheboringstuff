# When a() is called , it calls b(), which in turn calls c(). 
# The c() function doesn’t call anything; it just displays c() starts and c() returns before returning to the line in b() that called it.
# Once execution returns to the code in b() that called c(), it returns to the line in a() that called b().
# The execution continues to the next line in the b() function, which is a call to d().
# Like the c() function, the d() function also doesn’t call anything. It just displays d() starts and d() returns before returning to the line in b() that called it. 
# Since b() contains no other code, the execution returns to the line in a() that called b().
# The last line in a() displays a() returns before returning to the original a() call at the end of the program.

def a():
    print('a() starts') 
    b()
    d()
    print('a() returns')
def b():
    print('b() starts')
    c()
    print('b() returns')
def c():
    print('c() starts')
    print('c() returns')
def d():
    print('d() starts')
    print('d() returns')

a()