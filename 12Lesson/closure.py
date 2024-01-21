# Closure is a function having access to the scope of its parent function after the parent function has returned the function

def parentFun(person, coins):

    def paly_fun():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left ")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coins left ")

        else:
            print("\n" + person + " has ran out of coins ")

    return paly_fun


tommy = parentFun("Tommy", 5)
jimmy = parentFun("Jimmy", 2)
tommy()
tommy()
tommy()
jimmy()
