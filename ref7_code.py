import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.config import INITIAL_BALANCE, MenuOption
from services.validator import Validator
from services.menu import MenuService
from services.logger import log_action

# Клас історії транзакцій
class TransactionHistory:
    def __init__(self):
        self.history = []

    def add(self, text):
        self.history.append(text)

    def print_all(self):
        if not self.history:
            print("Історія транзакцій порожня.")
        else:
            for transaction in self.history:
                print(transaction)

# Основний клас банківського рахунку
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = TransactionHistory()

    @log_action
    def deposit(self, amount):
        if not Validator.is_valid_amount(amount):
            return
        self.balance += amount
        self.transactions.add(f"Поповнення: {amount}")
        print("Гроші успішно внесено на рахунок.")

    @log_action
    def withdraw(self, amount):
        if not Validator.is_valid_amount(amount):
            return
        if self.balance - amount >= 0:
            self.balance -= amount
            self.transactions.add(f"Зняття: {amount}")
            print("Гроші знято з рахунку.")
        else:
            print("Недостатньо коштів.")

    @log_action
    def check_balance(self):
        print("Поточний баланс:", self.balance)

    def print_history(self):
        self.transactions.print_all()

def main():
    account = BankAccount("Іван", INITIAL_BALANCE)
    menu = MenuService(account)

    running = True
    while running:
        menu.show_menu()
        choice = input("Ваш вибір: ")
        running = menu.handle_choice(choice)

if __name__ == "__main__":
    main()
