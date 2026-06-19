import random, os, customtkinter, time
#declare variables because python hates me
GAMBLE = False
lottery = random.randint(1, 70)
jackpot = random.randint(1, 15)
gambled = random.randint(1, 4)
MILLIONARE = random.randint(1, 1000)

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
        global gambled, jackpot, lottery, MILLIONARE, GAMBLE
        if MILLIONARE == 1:
            self.money += 9999999
        if gambled == 1:
            self.money += amount * 2
        if jackpot == 1:
            self.money += 9999
        if lottery == 1:
            self.money += 999999
        if amount >= 4999:
            self.money -= 99
        if GAMBLE == True:
            self.money -= 99999
            shuffle2 = random.randint(1, 4)
            if shuffle2 == 1:
                self.money += 99999

    def write(self):
        with open(full_path, "a") as file:
            file.write(f"Money left over is ${self.money}\n")
            if jackpot == 1:
                file.write("You also won the jackpot. (+9999)\n")
            if gambled == 1:
                file.write("You won the prize. (gambled amount * 2)\n")
            if lottery == 1:
                file.write("YOU HIT THE LOTTERY! (+999999)\n")
            if MILLIONARE == 1:
                file.write(f"YOU ARE THE BEST GAMBLER TO TOUCH THE PLANET!!!!!(+9999999)\n")
                time.sleep(3)

def run_gamble():
    global GAMBLE
    amount = random.randint(1, 1000)
    bigamount = random.randint(1, 500000)
    if amount <= 750:
        account.gamble(bigamount)
    label_var.configure(text=f"Your money is now ${account.money}")
    account.write()
def ruinyourlife():
    global GAMBLE
    GAMBLE = True
    for i in range(50):
        run_gamble()
        i + 1
    time.sleep(0.05)
    GAMBLE = False
def loop():
    global GAMBLE
    GAMBLE = True
    for i in range(500):
        run_gamble()
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
    gamble2_button = customtkinter.CTkButton(root, text="GO BIG OR GO HOME! (+50)", command=ruinyourlife)
    gamble2_button.pack(pady=20)
    gamble3_button = customtkinter.CTkButton(root, text="GAMBLING IS MY LIFE FORCE!!! (+500)", command=loop)
    gamble3_button.pack(pady=20)
    root.mainloop()
app()