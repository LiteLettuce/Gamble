import random, os, time

direct = "GAMBLINGLOG"
filed = "gamblinglog.txt"
if not os.path.exists(direct):
    os.makedirs(direct)
full_path = os.path.join(direct, filed)

class Account:
    def __init__(self, owner, money):
        self.owner = owner
        self.money = money

    def gamble(self, amount):
        self.money -= amount
        print(f"Gambled ${amount}")
        global gambled, jackpot, lottery
        gambled = random.randint(1, 4)
        jackpot = random.randint(1, 15)
        lottery = random.randint(1, 50)
        if gambled == 1:
            self.money += amount * 2
            print("You won your gamble.")
        else:
            print("You lost your gamble.")
        if jackpot == 1:
            self.money += 9999
            print("YOU JUST HIT THE JACKPOT!!!")
        else:
            print("You've lost the jackpot.")
        if lottery == 1:
            self.money += 999999
            print("HOLY SMOKES, YOU HIT THE LOTTERY!!!!!")
        return jackpot, gambled, lottery
    def check(self):
        print(f"Your money is: ${self.money}")

    def write(self):
        with open(full_path, "a") as file:
            file.write(f"Money left over is ${self.money}\n")
            if jackpot == 1:
                file.write("You also won the jackpot. (+9999)\n")
            if gambled == 1:
                file.write("You won the prize. (gambled amount * 2)\n")
            if lottery == 1:
                file.write("YOU HIT THE LOTTERY! (+999999)\n")
shuffle = random.randint(1000, 5000)
shuffle2 = random.randint(500, 1000)
account = Account("Lettuce", shuffle)

account.check()
account.gamble(shuffle2)
account.check()
account.write()
time.sleep(60000)