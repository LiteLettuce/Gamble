import random, os, customtkinter, time

direct = "GAMBLINGLOG"
filed = "gamblinglog.txt"
if not os.path.exists(direct):
    os.makedirs(direct)
full_path = os.path.join(direct, filed)

class Account:
    def __init__(self, money):
        self.money = money
        self.lost = False
        self.loanmoney = False
        self.gambled = 0
        self.jackpot = 0
        self.lottery = 0

    def gamble(self, amount):
        self.money -= amount
        print(f"Gambled ${amount}")
        self.lost = False
        self.gambled = random.randint(1, 4)
        self.jackpot = random.randint(1, 100)
        self.lottery = random.randint(1, 1000)
        if self.gambled == 1:
            self.money += amount * 2
        if self.jackpot == 1:
            self.money += 9999
        if self.lottery == 1:
            self.money += 999999
        if random.randint(1, 100) == 1:
            self.money -= 99
        if self.money <= 50000:
            self.money += 500
        if self.money <= -9999:
            self.lost == True
            self.money += amount 
    def loan(self, amount):
        self.money += amount
        label_var.configure(text=f"Your money is now ${self.money}")
        if self.money >= 0:
            return
        elif self.gambled == 1:
            self.money -= 5000
            label_var.configure(text=f"Paid intrest (-5000)\n Your money is now ${self.money}")
            self.loanmoney = True

    def write(self):
        with open(full_path, "a") as file:
            file.write(f"Money left over is ${self.money}\n")
            if self.jackpot == 1:
                file.write("You also won the jackpot. (+9999)\n")
            if self.gambled == 1:
                file.write("You won the prize. (gambled amount * 2)\n")
            if self.lottery == 1:
                file.write("YOU HIT THE LOTTERY! (+999999)\n")
            if self.lost == True:
                file.write("Your in debt, congrats\n")
            if self.loanmoney == True:
                file.write("Gotta pay intrest somehow. (-5000)\n")

def run_gamble():
    amount = random.randint(1, 1000)
    bigamount = random.randint(1, 10000)
    if random.randint(1, 4) <= 1:
        account.gamble(bigamount)
    else:
        account.gamble(amount)
        label_var.configure(text=f"Your money is now ${account.money}")
    account.write()
def ruinyourlife():
    for i in range(50):
        run_gamble()
        i + 1
def loop():
    for i in range(100):
        run_gamble()
        i + 1
def bypass():
    account.loan(random.randint(1, 10000))

def app():
    global label_var
    global account

    root = customtkinter.CTk()
    root.title("Gambling")
    root.geometry("500x400")
    root.resizable(False, False)

    starting_money = random.randint(1000, 5000)
    account = Account(starting_money)

    label_var = customtkinter.CTkLabel(root, text=f"Your money is ${account.money}", font=("Times New Roman", 15))
    label_var.pack(pady=20)

    gamble_button = customtkinter.CTkButton(root, text="Gamble", command=run_gamble)
    gamble_button.pack(pady=20)
    gamble2_button = customtkinter.CTkButton(root, text="GO BIG OR GO HOME! (+50)", command=ruinyourlife)
    gamble2_button.pack(pady=20)
    gamble3_button = customtkinter.CTkButton(root, text="GAMBLING IS MY LIFE FORCE!!! (+100)", command=loop)
    gamble3_button.pack(pady=20)
    loan_button = customtkinter.CTkButton(root, text="Click to get a loan", command=bypass)
    loan_button.pack(pady=20)
    root.mainloop()
app()