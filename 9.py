class BankAccount:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def show_info(self):
        print(f"Egasi: {self.owner}")
        print(f"Hisob raqami: {self.account_number}")
        print(f"Balans: {self.balance} so'm")

    def deposit(self, amount):
        if amount <= 0:
            print("Noto'g'ri summa.")
        else:
            self.balance += amount
            print(f"{amount} so'm hisobga qo'shildi.")
            print(f"Yangi balans: {self.balance} so'm")

    def withdraw(self, amount):
        if amount <= 0:
            print("Noto'g'ri summa.")
        elif amount > self.balance:
            print("Mablag' yetarli emas.")
        else:
            self.balance -= amount
            print(f"{amount} so'm yechildi.")
            print(f"Yangi balans: {self.balance} so'm")

    def show_balance(self):
        print(f"Balans: {self.balance} so'm")

    def transfer(self, other_account, amount):
        if amount <= 0:
            print("Noto'g'ri summa.")
        elif amount > self.balance:
            print("Pul o'tkazish uchun mablag' yetarli emas.")
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f"{amount} so'm muvaffaqiyatli o'tkazildi.")


account1 = BankAccount("Ali Valiyev", "86001234", 100000)
account2 = BankAccount("Olim Karimov", "86005678", 200000)
account3 = BankAccount("Zuhra Toshmatova", "86009012", 50000)

print("--- Account 1 Testlari ---")
account1.show_info()
account1.deposit(50000)
account1.withdraw(30000)
account1.withdraw(200000)
account1.show_balance()
print()

print("--- Account 2 & Transfer Testlari ---")
account2.show_balance()
account1.transfer(account2, 50000)
account1.show_balance()
account2.show_balance()
print()

print("--- Account 3 Testlari ---")
account3.show_info()
account3.deposit(100000)
account3.show_balance()