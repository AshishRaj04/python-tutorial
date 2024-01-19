def hello():
    print("Hello , World")


hello()


def sum(num1=3, num2=0):
    if (type(num1) != int or type(num2) != int):
        return 0
    return num1 + num2


total = sum("a", 6)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "Sara", "John")


def multiple_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multiple_named_items(first="Ashish", last="Raj")
