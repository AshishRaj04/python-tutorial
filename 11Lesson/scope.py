name = "Raj"  # global scope
count = 1  # these global scope variables can't be modified in a local scope .


def greeting(name):

    # count = 2 # this is not modifying the global variable count to 2 but defining a new variable count in the local scope of the function and assigning the value of 2

    # count += 1 # this will cause error becaue there is no previous value of count in the local scope of the function to increment it by 1.

    global count  # this is how to modify the global variable .
    count += 1
    newNum = 12
    print(count)
    color = "blue"  # local scope
    print(color)
    print("Welcome", name)

    def newFunc():
        nonlocal newNum  # similar to the concept of global . but as newNum is not global variable , nonlocal is used
        newNum += 1
        print(newNum)
    newFunc()


greeting("Ashish")
