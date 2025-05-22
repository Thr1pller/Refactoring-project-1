from project.services.config import (
    INITIAL_BALANCE,
    MENU_DEPOSIT,
    MENU_WITHDRAW,
    MENU_BALANCE,
    MENU_HISTORY,
    MENU_EXIT
)

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

# Клас банківського рахунку
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = TransactionHistory()

    def is_valid_amount(self, amount):
        if amount <= 0:
            print("Сума має бути більшою за нуль.")
            return False
        return True

    def deposit(self, amount):
        if not self.is_valid_amount(amount):
            return
        self.balance += amount
        self.transactions.add(f"Поповнення: {amount}")
        print("Гроші успішно внесено на рахунок.")

    def withdraw(self, amount):
        if not self.is_valid_amount(amount):
            return
        if self.balance - amount >= 0:
            self.balance -= amount
            self.transactions.add(f"Зняття: {amount}")
            print("Гроші знято з рахунку.")
        else:
            print("Недостатньо коштів.")

    def check_balance(self):
        print("Поточний баланс:", self.balance)

    def print_history(self):
        self.transactions.print_all()

def show_menu():
    print("\n1. Поповнити рахунок")
    print("2. Зняти кошти")
    print("3. Перевірити баланс")
    print("4. Показати історію")
    print("5. Вийти")

def get_amount_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Введено некоректну суму.")
        return 0

def handle_choice(account, choice):
    if choice == MENU_DEPOSIT:
        amount = get_amount_input("Введіть суму поповнення: ")
        account.deposit(amount)
    elif choice == MENU_WITHDRAW:
        amount = get_amount_input("Введіть суму зняття: ")
        account.withdraw(amount)
    elif choice == MENU_BALANCE:
        account.check_balance()
    elif choice == MENU_HISTORY:
        account.print_history()
    elif choice == MENU_EXIT:
        print("Дякуємо за використання банківської системи!")
        return False
    else:
        print("Невірний вибір.")
    return True

def main():
    account = BankAccount("Іван", INITIAL_BALANCE)
    running = True
    while running:
        show_menu()
        choice = input("Ваш вибір: ")
        running = handle_choice(account, choice)

if __name__ == "__main__":
    main()