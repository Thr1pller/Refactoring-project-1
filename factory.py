from services.config import INITIAL_BALANCE, MenuOption
from services.validator import Validator
from services.logger import log_action
from services.input_service import InputService
from services.storage import save_account, load_account


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

    def to_list(self):
        return self.history

    def from_list(self, data):
        self.history = data


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

    def save(self):
        save_account(self.name, self.balance, self.transactions.to_list())

    @staticmethod
    def load():
        data = load_account()
        if not data:
            return None
        account = BankAccount(data["name"], data["balance"])
        account.transactions.from_list(data["history"])
        return account


class AccountFactory:
    @staticmethod
    def create_account(name: str, balance: float = INITIAL_BALANCE) -> BankAccount:
        return BankAccount(name, balance)
