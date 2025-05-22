from services.commands import (
    DepositCommand, WithdrawCommand,
    BalanceCommand, HistoryCommand, ExitCommand
)
from services.config import MenuOption

class MenuService:
    def __init__(self, account):
        self.account = account
        self.commands = {
            MenuOption.DEPOSIT.value: DepositCommand(),
            MenuOption.WITHDRAW.value: WithdrawCommand(),
            MenuOption.BALANCE.value: BalanceCommand(),
            MenuOption.HISTORY.value: HistoryCommand(),
            MenuOption.EXIT.value: ExitCommand()
        }

    def show_menu(self):
        print("\n1. Поповнити рахунок")
        print("2. Зняти кошти")
        print("3. Перевірити баланс")
        print("4. Показати історію")
        print("5. Вийти")

    def handle_choice(self, choice):
        command = self.commands.get(choice)
        if command:
            result = command.execute(self.account)
            return result is not False  # Повертаємо False тільки якщо Exit
        else:
            print("Невірний вибір.")
            return True
