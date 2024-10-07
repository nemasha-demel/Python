#Used when order is not matter.
#Unique and immutable elements. 

#Creating a set
    #There are two ways to create a set. 
        #Inside curly braces, set()
set1 = {'hello',('one', 'two'),15}
print(set1)
set2 = set([1,2,3])
print(set2)
print("Length of the set: ",len(set2))

#Curly braces without don't create a empty set. This creates a dictionary
set3 = {}
print(type(set3))
#To create a empty set use set()
set4 = set()
print(type(set4))

set5 = set('abcbac') #This converts the string to a set of unique charactors
print(set5)

#Accessing elements
accset = {'a','b','c','d','e'}
for i in accset:
    print(i, end=' ')

#Checking the element
print('a' in accset)

#Adding elements
set6 = {'car','bicycle','bus'}
print("Before adding elements: ", set6)
#By using add() method only one element can be added
set6.add('van')
#By using update() method multiple elements can be added
set6.update(['helicoptor','bike'])
print("After adding elements: ", set6)

#Removing elemets
#If the removing element is not presented in the set, this will cause to an error
set6.remove('car') 
#If the removing element is not presented in the set, this will not cause to an error
set6.discard('long vehicle')
print("After removing elements using remove() and discard() methods: ", set6)
#pop() method will remove an element randomly
set6.pop()
print("After removing elements using pop() method: ", set6)

#Set Union
set7 = {1,2,3,4}
set8 = {2,3,5,6}
print(set7.union(set8))
print(set7|set8)

#Set Intersection
print(set7.intersection(set8))
print(set7&set8)

#Set difference
print(set7-set8)
print(set7.difference(set8))

