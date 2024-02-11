############################## MAP FUNCTION###############################

from functools import reduce
numbers = [3, 43, 63, 26, 74, 9, 1, 44, 32]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

############################# FILTER FUNCTION###############################


odd_num = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_num))

############################# FILTER FUNCTION###############################


total = reduce(lambda acc, curr: acc + curr, numbers)
# total = reduce(lambda acc, curr: acc + curr, numbers , 10) #add 10 as well

print(total)

print(sum(numbers))
print(sum(numbers) , 10) #add 10 as well
