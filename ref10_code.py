"""Головний модуль запуску банківського додатку — використовує Factory Pattern."""

import sys
import os
from services.menu import MenuService
from services.factory import AccountFactory, BankAccount
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    """Головна функція запуску банківського додатку з підтримкою памʼяті."""
    account = BankAccount.load()
    if not account:
        account = AccountFactory.create_account("Іван")

    menu = MenuService(account)

    running = True
    while running:
        menu.show_menu()
        choice = input("Ваш вибір: ")
        running = menu.handle_choice(choice)

    # Зберігаємо акаунт при виході
    account.save()


if __name__ == "__main__":
    main()
