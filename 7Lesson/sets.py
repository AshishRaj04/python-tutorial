nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums2))
print(len(nums2))

# No duplicates are allowed

nums = {1, 2, 2, 3}
print(nums)

# True is duplicate of 1 and False is duplicate of 0

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# Chech is a value in a set

print(2 in nums)

# but you can't refer to an element in the set with an index position or a key like you used to do in the case of lists and dictionaries

# Add a new element to a set

nums.add(8)
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)


# you can use update with lists , tuples and dictionaries , too

# Merge two sets to create a new set

one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplictes

one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)


# Keep only the difference

one = {1, 2, 3}
two = {2, 3, 4}
one.difference_update(two)
print(one)

# Keep everything except the difference

one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)
