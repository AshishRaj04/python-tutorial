users = ["Kajal" , "Shruti" , "Shivani" , "Payal" , "Ankita"]

data = ["Raj" , 2003 , "True"]

emptyList = []

print("Raj" in data)

print(users[-1])
print(users[-2])
print(users[-3])

print(users.index('Shruti'))

print(users[0 : 2]) # everything from 0 to position 2 . Does not include the position 2 .
print(users[1 : ]) # everything from 1 to the end of the list .
print(users[-3 : -1])

print(len(users))

users.append('Ex')
users += ['Anamika']
users.extend(["Richa" , "Komal"])
# users.extend(data)
print(users)
print(len(users))

users.insert(0 , "Jansi")
users[2:2] = ["Eddie" , "Alex"] #here , starts at 2 and end at 2  , so nothing gets replaced
print(users)
print(len(users))
users[1:3] = ["Robert" , "Sam"] # this gonna replace the values at 1 and 2 with Robert and Sam
print(users)
print(len(users))

users.remove("Jansi")
poppedUser = users.pop() #returns the last removed item
print(f"{users}" , poppedUser)
print(len(users))

del users[0]
data.clear() # empty the data list
del data # delete the data list
# print(data)  this will cause an error cuz data does't exist

users[1:1] = ["kajal"]
users.sort() #alphabatical sorting  , but lower cased words comes last (kajal) .
print(users)
users.sort(key=str.lower)
print(users)


nums = [2,423,52,5,2,26,62]
nums.reverse() #reversing the list not sorting in decending order
print(nums)

# nums.sort(reverse=True) #sort in decending order , and change the original nums
# print(nums)

print(sorted(nums , reverse=True)) #does not change the original nums
print(nums)

#coping

numsCopy = nums.copy()
myNums = list(nums)
myCopy = nums[:]
#al 4 print statements will be same
print(numsCopy)
print(myNums)
print(myCopy)
print(nums)

print(type(nums))

myList = list([1 , "Raj" , True])
print(myList)