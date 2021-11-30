# 'continue' statements are used inside loops. 
# When the program execution reaches a continue statement, 
# the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition. 
# (This is also what happens when the execution reaches the end of the loop.)
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')