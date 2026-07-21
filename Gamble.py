import random, os, customtkinter, datetime

direct = "GAMBLINGLOG"
filed = "gamblinglog.txt"
if not os.path.exists(direct):
    os.makedirs(direct)
full_path = os.path.join(direct, filed)

class Account:
    def __init__(self, money):
        self.money = money
        self.lost = False
        self.cap = False
        self.gambled = 0
        self.jackpot = 0
        self.lottery = 0
        self.takeout = 0
        self.factor = random.randint(1, 6)
        self.highstakes = False
        self.check = 0
        self.gambleinfo = "Waiting for gambles..."

    def gamble(self, amount):
        self.check = 1 #checking if you gambled
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
            app.MainGambleLabel.configure(text=f"Your in too much debt to gamble.\n Your money is {self.money}")
        else:    
            if self.highstakes == True:
                if random.randint(1, 4) == 1:
                    self.money -= amount * app.value2
                    app.CustomGambleLabel.configure(text=f"Lost your multipiler chance\n Money is now {int(self.money)}")
                    self.highstakes = False
                else:
                    self.money -= amount
                    app.CustomGambleLabel.configure(text=f"Won your multiplier chance\n Money is now {int(self.money)}")
            else:
                self.money -= amount

            entry = f"Gambled ${amount}"

            if self.gambled == 1:
                if self.highstakes == True:
                    self.money += amount * 2 * app.value2 * run.rebirthmultipler
                else:
                    self.money += amount * 2 * run.rebirthmultipler
                entry += " -> Won prize (x2)"
            if self.jackpot == 1:
                if self.highstakes == True:
                    self.money += 9999 * app.value2 * run.rebirthmultipler
                else:
                    self.money += 9999 * run.rebirthmultipler
                entry += " -> JACKPOT (+9999)"
            if self.lottery == 1:
                if self.highstakes == True:
                    self.money += 999999 * app.value2 * run.rebirthmultipler
                else:
                    self.money += 999999 * run.rebirthmultipler
                entry += " -> LOTTERY (+999999)"

            if self.gambleinfo == "Waiting for gambles...":
                self.gambleinfo = entry
            else:
                self.gambleinfo += f"\n{entry}"

            app.log_gamble(entry)

            if self.money <= -9999:
                self.lost = True
            if self.cap == True:
                self.lost = False

            self.money // 1 #rounds the money
    
    def gamblecustom(self):
        self.cap = True
        if app.value2 >= 2:
            self.highstakes = True
            account.gamble(app.value1)
            self.highstakes = False
        else:
            account.gamble(app.value1)
            app.CustomGambleLabel.configure(text=f"Your money is now ${int(account.money)}")

    def debt(self):
        self.cap = True

    def loan(self, amount):
        if self.takeout >= 5:
            app.MainGambleLabel.configure(text="You've taken a loan too many times.")
        else:
            self.money += amount
            self.takeout += 1
            app.MainGambleLabel.configure(text=f"Your money is now ${self.money}")
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
        self.rebirthmultipler = 1.0
        self.rebirthcost = 1.0

    def run_gamble(self):
        self.amount = random.randint(1, 1000)
        self.bigamount = random.randint(1, 10000)
        if random.randint(1, 4) == 1:
            account.gamble(self.bigamount)
        else:
            account.gamble(self.amount)
        if account.lost and account.cap == False:
            pass
        else:
            app.MainGambleLabel.configure(text=f"Your money is now ${int(account.money)}")
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
            app.MainGambleLabel.configure(text="Must need to remove debt limits first.")

    def bypass(self):
        account.loan(random.randint(1, 10000))

    def values(self):
        if account.factor == 1:
            app.MainGambleLabel.configure(text="Values are lower than normal.")
        elif account.factor == 6:
            app.MainGambleLabel.configure(text="Values are higher than normal.")
        else:
            app.MainGambleLabel.configure(text="Values are the normal.")

    def read(self):
        if account.check == 1:
            app.open_history()
        else:
            app.MainGambleLabel.configure(text="Need to gamble first")

    def check(self):
        if self.counter is None:
            self.counter = 0
            if os.path.exists(full_path):
                with open(full_path, "rb") as file:
                    self.counter = sum(1 for _ in file)
        return self.counter
    
    def switching(self):
        state = app.extra_switch.get()
        if state == 1:
            app.gamble_button.pack_forget()
            app.gamble2_button.pack_forget()
            app.gamble3_button.pack_forget()
            app.gamble4_button.pack_forget()
            app.accountmanager.pack_forget()
            app.check_button.pack(pady=12.5)
            app.debt_button.pack(pady=12.5)
            app.read_button.pack(pady=12.5)
            app.detail_button.pack(pady=12.5)
            app.custom_button.pack(pady=12.5)
            app.extra_switch.pack_forget()
            app.extra_switch.pack(pady=12.5)
            app.rebirth_switch.pack_forget()
            app.rebirth_switch.pack(pady=12.5)
        else:
            app.check_button.pack_forget()
            app.debt_button.pack_forget()
            app.read_button.pack_forget()
            app.detail_button.pack_forget()
            app.custom_button.pack_forget()
            app.gamble_button.pack(pady=12.5)
            app.gamble2_button.pack(pady=12.5)
            app.gamble3_button.pack(pady=12.5)
            app.gamble4_button.pack(pady=12.5)
            app.accountmanager.pack(pady=12.5)
            app.extra_switch.pack_forget()
            app.extra_switch.pack(pady=12.5)
            app.rebirth_switch.pack_forget()
            app.rebirth_switch.pack(pady=12.5)

    def Rebirth(self):
        #To rebirth
        app.window4.destroy()
        account.money = 0
        app.MainGambleLabel.configure(text="Rebirthed")
        self.rebirthmultipler += 0.2
        self.rebirthcost *= 1.5

    def CancelRebirth(self):
        #To cancel a rebirth
        app.window4.destroy()

class Application:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.MainGambleTheme = customtkinter.CTkFrame(self.root, width=451, height=451, fg_color="#235DA8")
        self.MainGambleTheme.pack()
        self.MainGambleTheme.pack_propagate(False)
        self.MainGambleLabel = customtkinter.CTkLabel(self.MainGambleTheme, text=f"Your money is ${account.money}", font=("Times New Roman", 15))
        self.gambleinfo_box = None
        self.rebirthmoneyneeded = 0

    def App(self):
        #Startup main window
        self.root.title("Gambling")
        self.root.geometry("450x450")
        self.root.resizable(False, False)
        self.Widgets()
        self.root.mainloop()

    def open_history(self):
        #Start up history window
        with open(full_path, "r") as filing:
            content = filing.read()

        window2 = customtkinter.CTkToplevel(self.root)
        window2.title("Gambling History")
        window2.geometry("500x540")
        window2.resizable(False, False)
        window2.grab_set()

        self.HistoryGambleTheme = customtkinter.CTkFrame(window2, width=501, height=541, fg_color="#235DA8")
        self.HistoryGambleTheme.pack()
        self.HistoryGambleTheme.pack_propagate(False)

        textbox = customtkinter.CTkTextbox(self.HistoryGambleTheme, width=460, height=480, fg_color="#235DA8", font=("Times New Roman", 13))
        textbox.pack(padx=10, pady=10)
        textbox.insert("0.0", content)
        textbox.configure(state="disabled")
    
    def advancedgamble(self):
        #Start up advanced gamble window
        window3 = customtkinter.CTkToplevel(self.root)
        window3.title("Advanced Gamble Panel")
        window3.geometry("400x400")
        window3.resizable(False, False)

        self.AdvancedGambleTheme = customtkinter.CTkFrame(window3, width=401, height=401, fg_color="#15A2BB")
        self.AdvancedGambleTheme.pack()
        self.AdvancedGambleTheme.pack_propagate(False)

        gambleinfo = customtkinter.CTkTextbox(self.AdvancedGambleTheme, width=350, height=350, fg_color="#15A2BB", font=("Times New Roman", 13))
        gambleinfo.pack()
        gambleinfo.insert("0.0", account.gambleinfo)
        gambleinfo.configure(state="disabled")

        self.gambleinfo_box = gambleinfo

        def clear_ref():
            self.gambleinfo_box = None
            window3.destroy()
        window3.protocol("WM_DELETE_WINDOW", clear_ref) 

    def log_gamble(self, entry):
        if self.gambleinfo_box is not None:
            try:
                if self.gambleinfo_box.winfo_exists():
                    self.gambleinfo_box.configure(state="normal")
                    self.gambleinfo_box.insert("end", f"\n{entry}")
                    self.gambleinfo_box.see("end")
                    self.gambleinfo_box.configure(state="disabled")
            except Exception:
                self.gambleinfo_box = None
    
    def manager(self):
        #Account manager window
        self.window5 = customtkinter.CTkToplevel(self.root)
        self.window5.title("Rebirth.")
        self.window5.geometry("350x300")
        self.window5.resizable(False, False)
        self.window5.grab_set()

        theme6 = customtkinter.CTkFrame(self.window5, width=351, height=301, fg_color="#0B751A")
        theme6.pack()
        theme6.pack_propagate(False)

    def rebirthpanel(self):
        #Start up rebirth window
        self.window4 = customtkinter.CTkToplevel(self.root)
        self.window4.title("Rebirth.")
        self.window4.geometry("350x300")
        self.window4.resizable(False, False)
        self.window4.grab_set()

        self.AccountManagerGambleTheme = customtkinter.CTkFrame(self.window4, width=351, height=301, fg_color="#2D0B6B")
        self.AccountManagerGambleTheme.pack()
        self.AccountManagerGambleTheme.pack_propagate(False)

        self.RebirthGambleLabel = customtkinter.CTkLabel(self.AccountManagerGambleTheme, text="Are you sure you want to rebirth.\n You will gain X1.2 income at the cost of 1.5X cost of next rebirth.", font=("Times New Roman", 13))
        self.RebirthGambleLabel.pack(pady=12.5)

        yes = customtkinter.CTkButton(self.AccountManagerGambleTheme, text="Yes", fg_color="#094E18", corner_radius=100, hover_color="#042E0D", command=run.Rebirth)
        yes.pack(pady=12.5)
        
        no = customtkinter.CTkButton(self.AccountManagerGambleTheme, text="No", fg_color="#A70202", corner_radius=100, hover_color="#790000", command=run.CancelRebirth)
        no.pack(pady=12.5)

    def Rebirth(self):
        #Rebirth payment
        self.rebirthmoneyneeded = 1000000 * run.rebirthcost
        if account.money >= self.rebirthmoneyneeded:
            app.rebirthpanel()
        else:
            self.MainGambleLabel.configure(text=f"You are not worthy of the power.\n Come back with {self.rebirthmoneyneeded}")

    def Widgets(self):
        self.MainGambleLabel.pack(pady=12.5)

        self.gamble_button = customtkinter.CTkButton(self.MainGambleTheme, text="Gamble", fg_color="#094E18", corner_radius=100, hover_color="#042E0D", command=run.run_gamble)
        self.gamble_button.pack(pady=12.5)

        self.gamble2_button = customtkinter.CTkButton(self.MainGambleTheme, text="GO BIG OR GO HOME! (+10)", fg_color="#0084FF", hover_color="#025DB3", corner_radius=100, command=run.ruinyourlife)
        self.gamble2_button.pack(pady=12.5)

        self.gamble3_button = customtkinter.CTkButton(self.MainGambleTheme, text="GAMBLING IS MY LIFE FORCE!!! (+50)", fg_color="#7F0D8A", hover_color="#4E0855", corner_radius=100, command=run.loop)
        self.gamble3_button.pack(pady=12.5)

        self.gamble4_button = customtkinter.CTkButton(self.MainGambleTheme, text="THE GAMBLE OF HISTORY!!!!! (+250)", fg_color="#C41B1B", hover_color="#801010", corner_radius=100, command=run.holygamble)
        self.gamble4_button.pack(pady=12.5)

        self.accountmanager = customtkinter.CTkButton(self.MainGambleTheme, text="Click to open the account manager", fg_color="#0BC20B", corner_radius=100, hover_color="#067C06", command=app.manager)
        self.accountmanager.pack(pady=12.5)

        self.extra_switch = customtkinter.CTkSwitch(self.MainGambleTheme, text="Switch to extra buttons", command=run.switching)
        self.extra_switch.pack(pady=12.5)

        self.rebirth_switch = customtkinter.CTkSwitch(self.MainGambleTheme, text="Rebirth?", command=app.Rebirth)
        self.rebirth_switch.pack(pady=12.5)

        self.check_button = customtkinter.CTkButton(self.MainGambleTheme, text="Click to see values of winning", fg_color="#FF7300", hover_color="#AD4E00", corner_radius=100, command=run.values)

        self.debt_button = customtkinter.CTkButton(self.MainGambleTheme, text="Click to remove debt limits.", fg_color="#09C9BF", hover_color="#0C817B", corner_radius=100, command=account.debt)

        self.read_button = customtkinter.CTkButton(self.MainGambleTheme, text="Click to view history", fg_color="#9EA011", hover_color="#89B413", corner_radius=100, command=run.read)

        self.detail_button = customtkinter.CTkButton(self.MainGambleTheme, text="Click to show advanced gambles", fg_color="#6000DD", hover_color="#4000DD", corner_radius=100, command=app.advancedgamble)

        self.custom_button = customtkinter.CTkButton(self.MainGambleTheme, text="Click to customize gambles.", fg_color="#A71611", hover_color="#7C0F0C", corner_radius=100, command=app.Builder)
    
    def BuilderWidgets(self):
        self.CustomGambleTheme = customtkinter.CTkFrame(self.buildwindow, width=400, height=400, fg_color="#184279")
        self.CustomGambleTheme.pack()
        self.CustomGambleTheme.pack_propagate(False)

        self.CustomGambleLabel = customtkinter.CTkLabel(self.CustomGambleTheme, text=f"Amount is: 500, Multipler is 1X", font=("Times New Roman", 15))
        self.CustomGambleLabel.pack(pady=15)

        self.value1 = 500
        amountpicker = customtkinter.CTkSlider(self.CustomGambleTheme, width=350, height=25, progress_color="#0B5F80", number_of_steps=40, fg_color="#136CB6", from_=1, to=10000, command=app.on_slider_change1)
        amountpicker.set(500)
        amountpicker.pack(pady=15)
        
        self.value2 = 1
        multipilerpicker = customtkinter.CTkSlider(self.CustomGambleTheme, width=350, height=25, progress_color="#0B5F80", number_of_steps=10, fg_color="#136CB6", from_=1, to=10, command=app.on_slider_change2)
        multipilerpicker.set(1)
        multipilerpicker.pack(pady=15)

        gamblecusto_button = customtkinter.CTkButton(self.CustomGambleTheme, text="Click to custom gamble", fg_color="#A71611", hover_color="#7C0F0C", corner_radius=100, command=account.gamblecustom)
        gamblecusto_button.pack(pady=15)

    def on_slider_change1(self, value):
        self.value1 = value
        self.CustomGambleLabel.configure(text=f"Amount is: {int(self.value1)}\n Multipler is {int(self.value2)}X")

    def on_slider_change2(self, value):
        self.value2 = value
        self.CustomGambleLabel.configure(text=f"Amount is: {int(self.value1)}\n Multipler is {int(self.value2)}X")

    def Builder(self):
        #Opens Custom Gambling
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