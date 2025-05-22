import json
import os

DATA_FILE = "data/account_data.json"

def save_account(name, balance, history):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump({
            "name": name,
            "balance": balance,
            "history": history
        }, file, indent=2)

def load_account():
    if not os.path.exists(DATA_FILE):
        return None
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data
