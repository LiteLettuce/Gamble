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
        self.highstakes = False

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
            app.label_var.configure(text=f"Your in too much debt to gamble.\n Your money is {self.money}")
        else:
            if self.highstakes == True:
                if random.randint(1, 4) == 1:
                    self.money -= amount * app.value2
                    app.label2_var.configure(text=f"Lost your multipiler chance\n Money is now {int(self.money)}")
                else: 
                    self.money -= amount
                    app.label2_var.configure(text=f"Won your multiplier chance\n Money is now {int(self.money)}")
            else:
                self.money -= amount
            print(f"Gambled ${amount}")
            if self.gambled == 1:
                if self.highstakes == True:
                    self.money += amount * app.value2 * 2
                else:
                    self.money += amount * 2
            if self.jackpot == 1:
                if self.highstakes == True:
                    self.money += 9999 * app.value2
                else:
                    self.money += 9999
            if self.lottery == 1:
                if self.highstakes == True:
                    self.money += 999999 * app.value2
                else:
                    self.money += 999999
            if self.money <= -9999:
                self.lost = True
            if self.cap == True:
                self.lost = False
    
    def gamblecustom(self):
        self.cap = True
        if app.value2 >= 2:
            self.highstakes = True
            account.gamble(app.value1)
        else:
            account.gamble(app.value1)
            app.label2_var.configure(text=f"Your money is now ${int(account.money)}")

    def debt(self):
        self.cap = True

    def loan(self, amount):
        self.loanmoney = False
        if self.takeout >= 5:
            app.label_var.configure(text="You've taken a loan too many times.")
            if self.lost == True:
                app.label_var.configure(text=f"Your in too much debt to gamble.\n Your money is {self.money}")
        else:
            self.money += amount
            self.takeout += 1
            app.label_var.configure(text=f"Your money is now ${self.money}")
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
        if account.bypassed == True:
            return 0
        else:
            app.label_var.configure(text=f"Your money is now ${account.money}")
        account.write()

    def ruinyourlife(self):
        for _ in range(10):
            run.run_gamble()

    def loop(self):
        for _ in range(50):
            run.run_gamble()

    def holygamble(self):
        if account.cap == True:
            for _ in range(250):
                run.run_gamble()
        else:
            app.label_var.configure(text="Must need to remove debt limits first.")

    def bypass(self):
        account.loan(random.randint(1, 10000))

    def values(self):
        if account.factor == 1:
            app.label_var.configure(text="Values are lower than normal.")
        elif account.factor == 6:
            app.label_var.configure(text="Values are higher than normal.")
        else:
            app.label_var.configure(text="Values are the normal.")

    def log(self):
        direc = os.path.dirname(os.path.abspath(sys.argv[0]))
        path = os.path.join(direc, "GAMBLINGLOG")
        path = os.path.realpath(path)
        os.startfile(path)

    def read(self):
        if account.check == 1:
            app.open_history()
        else:
            app.label_var.configure(text="Need to gamble first")

    def check(self):
        if self.counter is None:
            self.counter = 0
            if os.path.exists(full_path):
                with open(full_path, "rb") as file:
                    self.counter = sum(1 for _ in file)
        return self.counter
    def custombuilder(self):
        app.Builder()

class Application:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.theme = customtkinter.CTkFrame(self.root, width=501, height=601, fg_color="#235DA8")
        self.theme.pack()
        self.theme.pack_propagate(False)
        self.label_var = customtkinter.CTkLabel(self.theme, text=f"Your money is ${account.money}", font=("Times New Roman", 15))

    def App(self):
        self.root.title("Gambling")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.Widgets()
        self.root.mainloop()

    def open_history(self):
        with open(full_path, "r") as filing:
            content = filing.read()

        window2 = customtkinter.CTkToplevel(self.root)
        window2.title("Gambling History")
        window2.geometry("500x540")
        window2.resizable(False, False)
        window2.grab_set()

        theme2 = customtkinter.CTkFrame(window2, width=501, height=541, fg_color="#235DA8")
        theme2.pack()
        theme2.pack_propagate(False)

        textbox = customtkinter.CTkTextbox(theme2, width=460, height=480, fg_color="#235DA8", font=("Times New Roman", 13))
        textbox.pack(padx=10, pady=10)
        textbox.insert("0.0", content)
        textbox.configure(state="disabled")

    def Widgets(self):
        self.label_var.pack(pady=12.5)

        gamble_button = customtkinter.CTkButton(self.theme, text="Gamble", fg_color="#094E18", corner_radius=100, hover_color="#042E0D", command=run.run_gamble)
        gamble_button.pack(pady=12.5)

        gamble2_button = customtkinter.CTkButton(self.theme, text="GO BIG OR GO HOME! (+10)", fg_color="#0084FF", hover_color="#025DB3", corner_radius=100, command=run.ruinyourlife)
        gamble2_button.pack(pady=12.5)

        gamble3_button = customtkinter.CTkButton(self.theme, text="GAMBLING IS MY LIFE FORCE!!! (+50)", fg_color="#7F0D8A", hover_color="#4E0855", corner_radius=100, command=run.loop)
        gamble3_button.pack(pady=12.5)

        gamble4_button = customtkinter.CTkButton(self.theme, text="THE GAMBLE OF HISTORY!!!!! (+250)", fg_color="#C41B1B", hover_color="#801010", corner_radius=100, command=run.holygamble)
        gamble4_button.pack(pady=12.5)

        loan_button = customtkinter.CTkButton(self.theme, text="Click to get a loan", fg_color="#0BC20B", corner_radius=100, hover_color="#067C06", command=run.bypass)
        loan_button.pack(pady=12.5)

        check_button = customtkinter.CTkButton(self.theme, text="Click to see values of winning", fg_color="#FF7300", hover_color="#AD4E00", corner_radius=100, command=run.values)
        check_button.pack(pady=12.5)

        logs_button = customtkinter.CTkButton(self.theme, text="Click to open logs", fg_color="#19181D", hover_color="#000000", corner_radius=100, command=run.log)
        logs_button.pack(pady=12.5)

        debt_button = customtkinter.CTkButton(self.theme, text="Click to remove debt limits.", fg_color="#09C9BF", hover_color="#0C817B", corner_radius=100, command=account.debt)
        debt_button.pack(pady=12.5)

        read_button = customtkinter.CTkButton(self.theme, text="Click to view history", fg_color="#9EA011", hover_color="#89B413", corner_radius=100, command=run.read)
        read_button.pack(pady=12.5)

        custom_button = customtkinter.CTkButton(self.theme, text="Click to customize gambles.", fg_color="#A71611", hover_color="#7C0F0C", corner_radius=100, command=run.custombuilder)
        custom_button.pack(pady=12.5)
    
    def BuilderWidgets(self):
        theme3 = customtkinter.CTkFrame(self.buildwindow, width=400, height=400, fg_color="#184279")
        theme3.pack()
        theme3.pack_propagate(False)

        self.label2_var = customtkinter.CTkLabel(theme3, text=f"Amount is: 500, Multipler is 1X", font=("Times New Roman", 15))
        self.label2_var.pack(pady=15)

        self.value1 = 500
        amountpicker = customtkinter.CTkSlider(theme3, width=350, height=25, progress_color="#0B5F80", number_of_steps=40, fg_color="#136CB6", from_=1, to=10000, command=app.on_slider_change1)
        amountpicker.set(500)
        amountpicker.pack(pady=15)
        
        self.value2 = 1
        multipilerpicker = customtkinter.CTkSlider(theme3, width=350, height=25, progress_color="#0B5F80", number_of_steps=10, fg_color="#136CB6", from_=1, to=10, command=app.on_slider_change2)
        multipilerpicker.set(1)
        multipilerpicker.pack(pady=15)

        gamblecusto_button = customtkinter.CTkButton(theme3, text="Click to custom gamble (Amount works, not anything else.).", fg_color="#A71611", hover_color="#7C0F0C", corner_radius=100, command=account.gamblecustom)
        gamblecusto_button.pack(pady=15)

    def on_slider_change1(self, value):
        self.value1 = value
        self.label2_var.configure(text=f"Amount is: {int(self.value1)}\n Multipler is {int(self.value2)}X")

    def on_slider_change2(self, value):
        self.value2 = value
        self.label2_var.configure(text=f"Amount is: {int(self.value1)}\n Multipler is {int(self.value2)}X")

    def Builder(self):
        self.buildwindow = customtkinter.CTkToplevel(self.root)
        self.buildwindow.title("Value selector")
        self.buildwindow.geometry("400x400")
        self.buildwindow.resizable(False, False)
        self.buildwindow.grab_set()
        app.BuilderWidgets()

def startup():
    app.App()

 #Will error out if not formatted like this
 #This is so it runs at the modular level
if random.randint(1, 2) == 1:
    starting_money = random.randint(10000, 20000)
else:
    starting_money = random.randint(5000, 15000)
account = Account(starting_money)
run = Rerun()
app = Application()

startup()