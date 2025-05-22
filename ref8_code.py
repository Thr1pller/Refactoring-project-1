"""Головний модуль запуску банківського додатку — використовує Factory Pattern."""

import sys
import os
from services.menu import MenuService
from services.factory import AccountFactory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    """Головна функція запуску додатку: створення акаунту та запуск меню."""
    account = AccountFactory.create_account("Іван")
    menu = MenuService(account)

    running = True
    while running:
        menu.show_menu()
        choice = input("Ваш вибір: ")
        running = menu.handle_choice(choice)

if __name__ == "__main__":
    main()
