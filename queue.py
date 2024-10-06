#Implenting an queue using a list
#First In, First Out

def enqueue(stack, value):
    stack.append(value)

def dequeue(stack):
    return stack.pop(0)

my_queue = []

enqueue(my_queue,'a')
enqueue(my_queue,'b')
enqueue(my_queue,'c')

print(my_queue)

dequeue(my_queue)
print(my_queue)