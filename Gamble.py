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
        global factor
        factor = 0
        self.loanmoney = False
        self.gambled = 0
        self.jackpot = 0
        self.lottery = 0
        self.takeout = 0
        factor = random.randint(1, 6)
        if factor == 1:
            self.gambled = random.randint(1, 6)
            self.jackpot = random.randint(1, 150)
            self.lottery = random.randint(1, 1500)
            print("y")
        elif factor == 6:
            self.gambled = random.randint(1, 3)
            self.jackpot = random.randint(1, 70)
            self.lottery = random.randint(1, 750)
            print("n")
        else:
            self.gambled = random.randint(1, 4)
            self.jackpot = random.randint(1, 100)
            self.lottery = random.randint(1, 1000)
            print("s")

    def gamble(self, amount):
        if self.lost == True:
            label_var.configure(text=f"Your in too much debt to gamble.\n Your money is {self.money}")
        else:
            self.money -= amount
            print(f"Gambled ${amount}")
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
            self.money -= 500
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
            if factor == 1:
                file.write("Values changed (lower chance of winning...)\n")
            elif factor == 6:
                file.write("Values changed (higher chance of winning!)\n")
            else:
                file.write("Values changed (normal chance of winning.)\n")
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
        for i in range(10):
            run.run_gamble()
            i + 1
    def loop(self):
        for i in range(50):
            run.run_gamble()
            i + 1
    def bypass(self):
        account.loan(random.randint(1, 10000))
    def values(self):
        if factor == 1:
            label_var.configure(text="Values are lower than normal.")
        elif factor == 6:
            label_var.configure(text="Values are higher than normal.")
        else:
            label_var.configure(text="Values are the normal.")
def app():
    global label_var, account, run

    root = customtkinter.CTk()
    root.title("Gambling")
    root.geometry("500x450")
    root.resizable(False, False)

    starting_money = random.randint(2000, 10000)
    account = Account(starting_money)
    run = Rerun()

    theme = customtkinter.CTkFrame(root, width=501, height=451, fg_color="#235DA8")
    theme.pack()
    theme.pack_propagate(False)

    label_var = customtkinter.CTkLabel(theme, text=f"Your money is ${account.money}", font=("Times New Roman", 15))
    label_var.pack(pady=20)

    gamble_button = customtkinter.CTkButton(theme, text="Gamble", fg_color="#094E18", corner_radius=100, command=run.run_gamble)
    gamble_button.pack(pady=20)
    gamble2_button = customtkinter.CTkButton(theme, text="GO BIG OR GO HOME! (+10)", fg_color="#0084FF", corner_radius=100, command=run.ruinyourlife)
    gamble2_button.pack(pady=20)
    gamble3_button = customtkinter.CTkButton(theme, text="GAMBLING IS MY LIFE FORCE!!! (+50)", fg_color="#7F0D8A", corner_radius=100, command=run.loop)
    gamble3_button.pack(pady=20)
    loan_button = customtkinter.CTkButton(theme, text="Click to get a loan", fg_color="#0BC20B", corner_radius=100, command=run.bypass)
    loan_button.pack(pady=20)
    check_button = customtkinter.CTkButton(theme, text="Click to see values of winning", fg_color="#FF7300", corner_radius=100, command=run.values)
    check_button.pack(pady=20)
    root.mainloop()
app()