import customtkinter as ctk
from tkinter import messagebox
from services.factory import BankAccount
from services.logger import log_action

# Початкова тема
current_mode = "light"
ctk.set_appearance_mode(current_mode)
ctk.set_default_color_theme("blue")

# Завантаження акаунту або створення нового
account = BankAccount.load()
if not account:
    from services.factory import AccountFactory
    account = AccountFactory.create_account("Іван")

# Основне вікно
app = ctk.CTk()
app.title("Банківський додаток")
app.geometry("500x500")
app.minsize(400, 400)

# Перемикач теми
def toggle_theme():
    global current_mode
    current_mode = "dark" if current_mode == "light" else "light"
    ctk.set_appearance_mode(current_mode)
    theme_button.configure(text="🌙" if current_mode == "light" else "☀️")

theme_button = ctk.CTkButton(
    master=app,
    text="🌙",
    width=40,
    height=40,
    corner_radius=20,
    font=("Arial", 14),
    command=toggle_theme
)
theme_button.place(relx=0.95, rely=0.05, anchor="ne")

# Ввід суми
label = ctk.CTkLabel(app, text="Сума:", font=("Arial", 14))
label.pack(pady=(60, 5))

amount_entry = ctk.CTkEntry(app, font=("Arial", 14), width=200)
amount_entry.pack(pady=5)

result_label = ctk.CTkLabel(app, text="", text_color="blue", font=("Arial", 13))
result_label.pack(pady=10)

# Дії
def get_amount():
    try:
        return float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть числове значення.")
        return None

def deposit():
    amount = get_amount()
    if amount is not None:
        account.deposit(amount)
        account.save()
        result_label.configure(text=f"Поповнено на {amount} грн.")
        log_action(f"Депозит: {amount}")

def withdraw():
    amount = get_amount()
    if amount is not None:
        account.withdraw(amount)
        account.save()
        result_label.configure(text=f"Знято {amount} грн.")
        log_action(f"Зняття: {amount}")

def show_balance():
    result_label.configure(text=f"Поточний баланс: {account.balance} грн.")
    log_action("Перевірка балансу")

def show_history():
    history = "\n".join(account.transactions.to_list())
    if not history:
        history = "Історія порожня."
    messagebox.showinfo("Історія транзакцій", history)
    log_action("Перегляд історії")

def exit_app():
    app.quit()

# Кнопки дій
def create_button(text, command):
    btn = ctk.CTkButton(app, text=text, command=command,
                        font=("Arial", 13),
                        width=200, height=40, corner_radius=20)
    btn.pack(pady=7)

create_button("Поповнити", deposit)
create_button("Зняти кошти", withdraw)
create_button("Перевірити баланс", show_balance)
create_button("Показати історію", show_history)
create_button("Вийти", exit_app)

# Запуск
app.mainloop()
