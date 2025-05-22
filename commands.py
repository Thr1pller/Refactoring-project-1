from services.input_service import InputService
from services.config import MenuOption

class Command:
    def execute(self, account):
        raise NotImplementedError("Команда повинна реалізовувати метод execute")

class DepositCommand(Command):
    def execute(self, account):
        amount = InputService.get_float("Введіть суму поповнення: ")
        account.deposit(amount)

class WithdrawCommand(Command):
    def execute(self, account):
        amount = InputService.get_float("Введіть суму зняття: ")
        account.withdraw(amount)

class BalanceCommand(Command):
    def execute(self, account):
        account.check_balance()

class HistoryCommand(Command):
    def execute(self, account):
        account.print_history()

class ExitCommand(Command):
    def execute(self, account):
        print("Дякуємо за використання банківського застосунку!")
        return False  # для виходу з програми
