person = "Ashish"
coins = 3

message = "\n%s has %s coins left." %(person , coins)
print(message)

message = "\n{} has {} coins left.".format(person , coins)
print(message)

message = "\n{1} has {0} coins left.".format(person , coins)
print(message)

message = "\n{person} has {coins} coins left.".format(person=person , coins=coins)
print(message)

player = {"person" : "Dave" , "coins" : 3 }

message = "\n{person} has {coins} coins left.".format(**player)
print(message)

##############################f_string###########################################

message = f"\n{person} has {2*10} coins left."
print(message)

num = 10
print(f"\n2.25 times {num} is {2.25*num:.3f}\n") #.3f means upto three decimal player . here f stand for fixed.

for num in range(1,11):
    print(f"{num} is {num / 5:.5%} percentage of 5") #.2% give the percentage value up to 2 decimal place