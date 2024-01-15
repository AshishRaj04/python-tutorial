#literal assignment
first = "Ashish"

print(type(first))
print(type(first) == str)
print(isinstance(first , str))

#constructor function
second = str("Raj")
print(type(second))
print(type(second) == str)
print(isinstance(second , str))

#concatenation
fullname = first + " " + second
print(fullname)

fullname += "!"
print(fullname)

#Casting a number to a string
dob = str(2003)
print(type(dob))
print(dob)

statement = "I am a fool born in " + dob  + "."
print(statement)

# Multiple lines
multiline = '''
    Hii , Shruti ? I just wanna be your friend . I am not forcing you . If your answer is no , I will be totally ook .
'''
print(multiline)

# Escaping special characters
sentence = 'I\'m a fullstact developer .\n \t Hey! where\'s your projects'
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("Hii" , "Hey"))
print(multiline.title())

print(len(multiline))
multiline += "                 "
multiline = "                 " + multiline
print(len(multiline))

# Remove white space
print(multiline.strip())
print(len(multiline))
print(multiline.lstrip())
print(len(multiline))
print(multiline.rstrip())
print(len(multiline))

# Build a menu
title = "menu".upper()
print(title.center(20 , "="))
print("Coffee".ljust(16 , ".") + "$1".rjust(4))


# string index value
print(first[-1])
print(first[1 : 4])

# Some method return bool value
print(first.startswith("D"))
print(first.endswith("h"))

