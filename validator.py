class Validator:
    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        if amount <= 0:
            print("Сума має бути більшою за нуль.")
            return False
        return True
