# Початкова версія банківської системи з "code smells"

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
            for h in self.history:
                print(h)

def main():
    account = BankAccount("Іван", 500)

    while True:
        print("\n1. Поповнити рахунок")
        print("2. Зняти кошти")
        print("3. Перевірити баланс")
        print("4. Показати історію")
        print("5. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            amount = float(input("Введіть суму поповнення: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Введіть суму зняття: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.print_history()
        elif choice == "5":
            print("Дякуємо за використання банківської системи!")
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()
