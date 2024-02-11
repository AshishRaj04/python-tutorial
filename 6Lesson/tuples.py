# In Python, a tuple is a collection data type that is ordered and immutable. It is similar to a list but with the key difference that tuples cannot be modified once they are created. 

myTuple = tuple(('Raj' , 2003 , True))
anotherTuple = (1,2,3,4,5,6 ,2,4,5,4)
print(myTuple)
print(anotherTuple)
print(type(myTuple))
print(type(anotherTuple))

newList = list(myTuple)
newList.append("Ashish")
newTuple = tuple(newList)
print(newTuple)

(one , *two , hey) = anotherTuple #rest of the number goes to two
print(one)
print(two)
print(hey)
print(type(hey)) #int data type
print(type(two)) #list data type

print(anotherTuple.count(4)) #how many types 4 appear
print(anotherTuple.index(1))