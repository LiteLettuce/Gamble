import random, os, sys, customtkinter, datetime

direct = "GAMBLINGLOG"
filed = "gamblinglog.txt"
if not os.path.exists(direct):
    os.makedirs(direct)
full_path = os.path.join(direct, filed)

class Account:
    def __init__(self, money):
        self.money = money
        self.lost = False
        self.check = 0
        self.cap = False
        self.gambled = 0
        self.jackpot = 0
        self.lottery = 0
        self.takeout = 0
        self.factor = random.randint(1, 6)

    def gamble(self, amount):
        self.check = 1
        if self.factor == 1:
            self.gambled = random.randint(1, 6)
            self.jackpot = random.randint(1, 100)
            self.lottery = random.randint(1, 1000)
        elif self.factor == 6:
            self.gambled = random.randint(1, 3)
            self.jackpot = random.randint(1, 50)
            self.lottery = random.randint(1, 500)
        else:
            self.gambled = random.randint(1, 4)
            self.jackpot = random.randint(1, 70)
            self.lottery = random.randint(1, 750)
        if self.lost == True and self.cap == False:
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
            if self.cap == True:
                self.lost = False
    def debt(self):
        self.cap = True
    def loan(self, amount):
        self.loanmoney = False
        if self.takeout >= 5:
            label_var.configure(text="You've taken a loan too many times.")
            if self.lost == True:
                label_var.configure(text=f"Your in too much debt to gamble.\n Your money is {self.money}")
        else:
            self.money += amount
            self.takeout += 1
            label_var.configure(text=f"Your money is now ${self.money}")
        print(f"Got loan of {amount}")

    def write(self):
        run.check()
        if run.counter >= 500:
            with open(full_path, "w") as file:
                file.truncate()
            run.counter = 0
        entry = f"On {datetime.datetime.now()}:\nMoney left over is ${self.money}\n"
        lines_added = 2
        if self.jackpot == 1:
            entry += "You also won the jackpot. (+9999)\n"
            lines_added += 1
        if self.gambled == 1:
            entry += "You won the prize. (gambled amount * 2)\n"
            lines_added += 1
        if self.lottery == 1:
            entry += "YOU HIT THE LOTTERY! (+999999)\n"
            lines_added += 1
        if self.lost == True:
            entry += "Your in debt, congrats\n"
            lines_added += 1
        with open(full_path, "a") as file:
            file.write(entry)
        run.counter += lines_added
class Rerun(): 
    def __init__(self):
        self.counter = 0    
    def run_gamble(self):
        self.amount = random.randint(1, 1000)
        self.bigamount = random.randint(1, 10000)
        if random.randint(1, 4) == 1:
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
    def holygamble(self):
        if account.cap == True:
            for i in range(250):
                run.run_gamble()
                i + 1
        else:
            label_var.configure(text="Must need to remove debt limits first.")
    def bypass(self):
        account.loan(random.randint(1, 10000))
    def values(self):
        if account.factor == 1:
            label_var.configure(text="Values are lower than normal.")
        elif account.factor == 6:
            label_var.configure(text="Values are higher than normal.")
        else:
            label_var.configure(text="Values are the normal.")
    def log(self):
        direc = os.path.dirname(os.path.abspath(sys.argv[0]))
        path = os.path.join(direc, "GAMBLINGLOG")
        path = os.path.realpath(path)
        os.startfile(path)
    def read(self):
        if account.check == 1:
            with open(full_path, "r") as file:
                app2()
        else:
            label_var.configure(text="Need to gamble first")
    def check(self):
        if self.counter is None:
            self.counter = 0
            if os.path.exists(full_path):
                with open(full_path, "rb") as file:
                    self.counter = sum(1 for _ in file)
        return self.counter
def app2():
    with open(full_path, "r") as filing:
        content = filing.read()

    window2 = customtkinter.CTkToplevel()
    window2.title("Gambling History")
    window2.geometry("500x540")
    window2.resizable(False, False)

    theme2 = customtkinter.CTkFrame(window2, width=501, height=541, fg_color="#235DA8")
    theme2.pack()
    theme2.pack_propagate(False  )

    textbox = customtkinter.CTkTextbox(theme2, width=460, height=480, fg_color="#235DA8", font=("Times New Roman", 13))
    textbox.pack(padx=10, pady=10)
    textbox.insert("0.0", content)
    textbox.configure(state="disabled")
def app():
    global label_var, account, run, cap, read_button
    
    root = customtkinter.CTk()
    root.title("Gambling")
    root.geometry("500x540")
    root.resizable(False, False)

    if random.randint(1, 2) == 1:
        starting_money = random.randint(10000, 20000)
    else:
        starting_money = random.randint(5000, 15000)
    account = Account(starting_money)
    run = Rerun()

    theme = customtkinter.CTkFrame(root, width=501, height=541, fg_color="#235DA8")
    theme.pack()
    theme.pack_propagate(False)

    label_var = customtkinter.CTkLabel(theme, text=f"Your money is ${account.money}", font=("Times New Roman", 15))
    label_var.pack(pady=12.5)

    gamble_button = customtkinter.CTkButton(theme, text="Gamble", fg_color="#094E18", corner_radius=100, hover_color="#042E0D", command=run.run_gamble)
    gamble_button.pack(pady=12.5)
    gamble2_button = customtkinter.CTkButton(theme, text="GO BIG OR GO HOME! (+10)", fg_color="#0084FF", hover_color="#025DB3", corner_radius=100, command=run.ruinyourlife)
    gamble2_button.pack(pady=12.5)
    gamble3_button = customtkinter.CTkButton(theme, text="GAMBLING IS MY LIFE FORCE!!! (+50)", fg_color="#7F0D8A", hover_color="#4E0855", corner_radius=100, command=run.loop)
    gamble3_button.pack(pady=12.5)
    gamble4_button = customtkinter.CTkButton(theme, text="THE GAMBLE OF HISTORY!!!!! (+250)", fg_color="#C41B1B", hover_color="#801010", corner_radius=100, command=run.holygamble)
    gamble4_button.pack(pady=12.5)
    loan_button = customtkinter.CTkButton(theme, text="Click to get a loan", fg_color="#0BC20B", corner_radius=100, hover_color="#067C06", command=run.bypass)
    loan_button.pack(pady=12.5)
    check_button = customtkinter.CTkButton(theme, text="Click to see values of winning", fg_color="#FF7300", hover_color="#AD4E00", corner_radius=100, command=run.values)
    check_button.pack(pady=12.5)
    logs_button = customtkinter.CTkButton(theme, text="Click to open logs", fg_color="#19181D", hover_color="#000000", corner_radius=100, command=run.log)
    logs_button.pack(pady=12.5)
    debt_button = customtkinter.CTkButton(theme, text="Click to remove debt limits.", fg_color="#09C9BF", hover_color="#0C817B", corner_radius=100, command=account.debt)
    debt_button.pack(pady=12.5)
    read_button = customtkinter.CTkButton(theme, text="Click to view history", fg_color="#9EA011", hover_color="#89B413", corner_radius=100, command=run.read)
    read_button.pack(pady=12.5)
    root.mainloop()
app()