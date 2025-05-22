class InputService:
    @staticmethod
    def get_float(prompt: str) -> float:
        try:
            return float(input(prompt))
        except ValueError:
            print("Введено некоректну суму.")
            return 0.0
