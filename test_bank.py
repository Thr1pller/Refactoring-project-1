import unittest
from services.factory import BankAccount, TransactionHistory
from services.validator import Validator
from services.storage import save_account, load_account
import os

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Тест", 1000)

    # Тести на поповнення
    def test_deposit_valid(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_deposit_invalid_negative(self):
        self.account.deposit(-100)
        self.assertEqual(self.account.balance, 1000)

    def test_deposit_zero(self):
        self.account.deposit(0)
        self.assertEqual(self.account.balance, 1000)

    def test_multiple_deposits(self):
        self.account.deposit(200)
        self.account.deposit(300)
        self.assertEqual(self.account.balance, 1500)

    # Тести на зняття коштів
    def test_withdraw_valid(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 800)

    def test_withdraw_too_much(self):
        self.account.withdraw(9999)
        self.assertEqual(self.account.balance, 1000)

    def test_withdraw_negative(self):
        self.account.withdraw(-100)
        self.assertEqual(self.account.balance, 1000)

    def test_multiple_withdrawals(self):
        self.account.withdraw(100)
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 700)

    # Тести на перевірку балансу
    def test_check_balance(self):
        self.assertIsInstance(self.account.balance, int)

    def test_balance_after_combined_actions(self):
        self.account.deposit(500)
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 1300)

    # Тести на історію транзакцій
    def test_transaction_history_add(self):
        self.account.transactions.add("Дія")
        self.assertEqual(len(self.account.transactions.history), 1)

    def test_transaction_history_to_list(self):
        self.account.transactions.add("1")
        self.assertEqual(self.account.transactions.to_list(), ["1"])

    def test_transaction_history_from_list(self):
        self.account.transactions.from_list(["А", "Б"])
        self.assertEqual(self.account.transactions.history, ["А", "Б"])

    def test_transaction_history_clear_then_add(self):
        self.account.transactions.from_list([])
        self.account.transactions.add("Start")
        self.assertIn("Start", self.account.transactions.history)

    # Тести на збереження/завантаження
    def test_save_and_load_account(self):
        self.account.deposit(123)
        self.account.save()
        loaded = BankAccount.load()
        self.assertEqual(loaded.balance, self.account.balance)

    def test_account_load_fallback(self):
        if os.path.exists("data/account_data.json"):
            os.remove("data/account_data.json")
        loaded = BankAccount.load()
        self.assertIsNone(loaded)

    def test_account_name_persistence(self):
        self.account.save()
        loaded = BankAccount.load()
        self.assertEqual(loaded.name, "Тест")

    # Тести на валідацію
    def test_validator_positive(self):
        self.assertTrue(Validator.is_valid_amount(10))

    def test_validator_negative(self):
        self.assertFalse(Validator.is_valid_amount(-10))

    def test_validator_zero(self):
        self.assertFalse(Validator.is_valid_amount(0))


if __name__ == '__main__':
    unittest.main()
