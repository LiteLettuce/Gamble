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
        self.takeout = 0

    def gamble(self, amount):
        if self.lost == True:
            label_var.configure(text=f"Your in too much debt to gamble.\n Your money is {self.money}")
        else:
            self.money -= amount
            print(f"Gambled ${amount}")
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
                self.lost = True 
    def loan(self, amount):
        self.loanmoney = False
        if self.takeout >= 5:
            label_var.configure(text="You've taken a loan too many times.")
            if self.lost == True:
                label_var.configure(text=f"Your in too much debt to gamble.\n Your money is {self.money}")
        else:
            self.money += amount
            self.money -= 5000
            self.loanmoney = True
            self.takeout += 1
            label_var.configure(text=f"Your money is now ${self.money}")
        print(f"Got loan of {amount}")

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
                file.write("Gotta pay interest somehow. (-5000)\n")
class Rerun():
    def __init__(self):
        self.amount = random.randint(1, 1000)
        self.bigamount = random.randint(1, 10000)
    def run_gamble(self):
        if random.randint(1, 4) <= 1:
            account.gamble(self.bigamount)
        else:
            account.gamble(self.amount)
            label_var.configure(text=f"Your money is now ${account.money}")
        account.write()
    def ruinyourlife(self):
        for i in range(50):
            run.run_gamble()
            i + 1
    def loop(self):
        for i in range(100):
            run.run_gamble()
            i + 1
    def bypass(self):
        account.loan(random.randint(1, 10000))

def app():
    global label_var, account, run

    root = customtkinter.CTk()
    root.title("Gambling")
    root.geometry("500x400")
    root.resizable(False, False)

    starting_money = random.randint(2000, 10000)
    account = Account(starting_money)
    run = Rerun()

    theme = customtkinter.CTkFrame(root, width=501, height=401, fg_color="#235DA8")
    theme.pack()
    theme.pack_propagate(False)

    label_var = customtkinter.CTkLabel(theme, text=f"Your money is ${account.money}", font=("Times New Roman", 15))
    label_var.pack(pady=20)

    gamble_button = customtkinter.CTkButton(theme, text="Gamble", fg_color="#094E18", corner_radius=100, command=run.run_gamble)
    gamble_button.pack(pady=20)
    gamble2_button = customtkinter.CTkButton(theme, text="GO BIG OR GO HOME! (+50)", fg_color="#0084FF", corner_radius=100, command=run.ruinyourlife)
    gamble2_button.pack(pady=20)
    gamble3_button = customtkinter.CTkButton(theme, text="GAMBLING IS MY LIFE FORCE!!! (+100)", fg_color="#7F0D8A", corner_radius=100, command=run.loop)
    gamble3_button.pack(pady=20)
    loan_button = customtkinter.CTkButton(theme, text="Click to get a loan", fg_color="#0BC20B", corner_radius=100, command=run.bypass)
    loan_button.pack(pady=20)
    root.mainloop()
app()