from functools import wraps

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"[LOG] Виклик: {func.__name__} | Аргументи: {args[1:]}, {kwargs} | Результат: {result}\n")
        return result
    return wrapper
