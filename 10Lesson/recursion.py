# def add_one(num):
#     if (num >= 9):
#         return num+1

#     total = num + 1
#     print(total)

#     return add_one(total)


# newTotal = add_one(0)
# print(newTotal)

def add_one(num):
    while num <= 9:
        total = num + 1
        print(total)
        num = num + 1


add_one(0)
