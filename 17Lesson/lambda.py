squared = lambda num : num * num
 
print(squared(3))

addTwo = lambda num : num + 2

print(addTwo(5))

sum = lambda a , b : a+b

print(sum(3,5))

########################################################################

def funcBuilder(x):
   return lambda num : num + x

addTen = funcBuilder(10)
addTwenty =funcBuilder(20)

print(addTen(2))
print(addTwenty(4))

