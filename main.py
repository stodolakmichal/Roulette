import numpy.random
import sys
sys.setrecursionlimit(10000000)

operations = 0

def losowanie(initial_money, money, GameOver):
    global operations
    operations += 1
    print(money)
    if(money<initial_money):
        print("Not enough money")
        return

    money-=initial_money
    number = numpy.random.choice(numpy.arange(1, 3), p=[0.5, 0.5])
    if(number!=1):
        initial_money*=2
    else:
        money = money + initial_money*2
        initial_money = initialMoney

    if(money == GameOver):
        return operations

    losowanie(initial_money, money, GameOver)

if __name__ == '__main__':
    #money = input("Write how much money you have: ")
    money = 1000
    print("Money: ", money)
    #initial_money = input("Write which value you want to start: ")
    initialMoney = 1
    print("Starting bid: ", initialMoney)
    #GameOver = input("Write how much you want to win: ")
    gameOver = 2000
    print("Play till: ", gameOver)

    for i in range(100):
        losowanie(initialMoney, money, gameOver)

    print("Number of operations: ", operations)

