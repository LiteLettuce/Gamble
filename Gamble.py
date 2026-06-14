import random, os

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
        gambled = random.randint(1, 4)
        global jackpot
        jackpot = random.randint(1, 15)
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
        return jackpot
    def check(self):
        print(f"Your money is: ${self.money}")

    def write(self):
        with open(full_path, "a") as file:
            file.write(f"Money left over is ${self.money}\n")
            if jackpot == 1:
                file.write("You also won the jackpot. (+9999)\n")

shuffle = random.randint(1000, 5000)
shuffle2 = random.randint(500, 1000)
account = Account("Lettuce", shuffle)

account.check()
account.gamble(shuffle2)
account.check()
account.write()