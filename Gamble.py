import random, os, customtkinter, time

direct = "GAMBLINGLOG"
filed = "gamblinglog.txt"
if not os.path.exists(direct):
    os.makedirs(direct)
full_path = os.path.join(direct, filed)

class Account:
    def __init__(self, money):
        self.money = money

    def gamble(self, amount):
        self.money -= amount
        print(f"Gambled ${amount}")
        global gambled, jackpot, lottery, lost, debt
        lost = False
        debt = False
        lottery = random.randint(1, 70)
        jackpot = random.randint(1, 15)
        gambled = random.randint(1, 4)
        if gambled == 1:
            self.money += amount * 2
        if jackpot == 1:
            self.money += 9999
        if lottery == 1:
            self.money += 999999
        if amount >= 4999:
            lost == True
            self.money -= 999
            shuffle = random.randint(1, 4)
            if shuffle == 1:
                debt == True
                self.money -= 9999
        if GAMBLE == True:
            self.money -= 99999
        return jackpot, gambled, lottery, lost, debt

    def write(self):
        with open(full_path, "a") as file:
            if GAMBLE == True:
                return
            else:
                file.write(f"Money left over is ${self.money}\n")
                if jackpot == 1:
                    file.write("You also won the jackpot. (+9999)\n")
                if gambled == 1:
                    file.write("You won the prize. (gambled amount * 2)\n")
                if lottery == 1:
                    file.write("YOU HIT THE LOTTERY! (+999999)\n")
                if lost == True:
                    file.write(f"You lost it all. (-999)\n")
                if debt == True:
                    file.write(f"You are probably in debt. (-9999)\n")

def run_gamble():
    amount = random.randint(1, 1000)
    bigamount = random.randint(1, 50000)
    if amount <= 500:
        account.gamble(bigamount)
    account.gamble(amount)

    label_var.configure(text=f"Your money is now ${account.money}")
    account.write()
def ruinyourlife():
    global GAMBLE
    GAMBLE = False
    label_var.configure(text="Brace for impact")
    GAMBLE = True
    for i in range(50):
        run_gamble()
        time.sleep(0)
        i + 1
    time.sleep(0.05)
    GAMBLE = False

def app():
    global label_var
    global account

    root = customtkinter.CTk()
    root.title("Gambling")
    root.geometry("500x400")

    starting_money = random.randint(1000, 5000)
    account = Account(starting_money)

    label_var = customtkinter.CTkLabel(root, text=f"Your money is ${account.money}", font=("Times New Roman", 15))
    label_var.pack(pady=20)

    gamble_button = customtkinter.CTkButton(root, text="Gamble", command=run_gamble)
    gamble_button.pack(pady=20)
    gamble2_button = customtkinter.CTkButton(root, text="GO BIG OR GO HOME!", command=ruinyourlife)
    gamble2_button.pack(pady=20)

    root.mainloop()
app()