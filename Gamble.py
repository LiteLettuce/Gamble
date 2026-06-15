import random, os, customtkinter

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
        global gambled, jackpot, lottery, lost
        lost = False
        gambled = random.randint(1, 4)
        jackpot = random.randint(1, 15)
        lottery = random.randint(1, 50)
        if gambled == 1:
            self.money += amount * 2
            print("You won your gamble.")
        else:
            print("You lost the gamble.")
        if jackpot == 1:
            self.money += 9999
            print("YOU JUST HIT THE JACKPOT!!!")
        else:
            print("You've lost the jackpot.")
        if lottery == 1:
            self.money += 999999
            print("HOLY SMOKES, YOU HIT THE LOTTERY!!!!!")
        else:
            print("You've lost the lottery.")
        if amount >= 4999:
            lost == True
            self.money -= 999
        return jackpot, gambled, lottery, lost

    def write(self):
        with open(full_path, "a") as file:
            file.write(f"Money left over is ${self.money}\n")
            if jackpot == 1:
                file.write("You also won the jackpot. (+9999)\n")
            if gambled == 1:
                file.write("You won the prize. (gambled amount * 2)\n")
            if lottery == 1:
                file.write("YOU HIT THE LOTTERY! (+999999)\n")
            if lost == True:
                file.write(f"You lost it all. (-999)\n")

def run_gamble():
    amount = random.randint(1, 1000)
    print(amount)
    bigamount = random.randint(1, 50000)
    if amount <= 500:
        account.gamble(bigamount)
    account.gamble(amount)

    label_var.configure(text=f"Your money is now ${account.money}")
    account.write()

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

    root.mainloop()

app()