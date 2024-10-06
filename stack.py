#Implenting a stack using a list
#Last In, First Out

def push(stack,value):
    stack.append(value)

#Removes the last element
def pop(stack):
    return stack.pop()

my_stack = []

push(my_stack,'a')
push(my_stack,'b')
push(my_stack,'c')

print(my_stack)

print(pop(my_stack))
pop(my_stack)
print(my_stack)
