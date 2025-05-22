# Константи
INITIAL_BALANCE = 500
MENU_DEPOSIT = "1"
MENU_WITHDRAW = "2"
MENU_BALANCE = "3"
MENU_HISTORY = "4"
MENU_EXIT = "5"

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append("Поповнення: " + str(amount))
            print("Гроші успішно внесено на рахунок.")
        else:
            print("Сума має бути більшою за нуль.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount >= 0:
                self.balance -= amount
                self.history.append("Зняття: " + str(amount))
                print("Гроші знято з рахунку.")
            else:
                print("Недостатньо коштів.")
        else:
            print("Сума має бути більшою за нуль.")

    def check_balance(self):
        print("Поточний баланс: " + str(self.balance))

    def print_history(self):
        if len(self.history) == 0:
            print("Історія транзакцій порожня.")
        else:
            for transaction in self.history:
                print(transaction)

# Метод для відображення меню
def show_menu():
    print("\n1. Поповнити рахунок")
    print("2. Зняти кошти")
    print("3. Перевірити баланс")
    print("4. Показати історію")
    print("5. Вийти")

# Метод для безпечного введення суми
def get_amount_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Введено некоректну суму.")
        return 0

# Метод для обробки вибору користувача
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
