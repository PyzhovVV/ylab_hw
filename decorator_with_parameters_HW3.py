from time import sleep


def my_decorator(call_count: int = 5, start_sleep_time: float = 1, factor: float = 2, border_sleep_time: float = 10):
    """Декоратор, выполняющий фанкцию (call_count) раз и использующий наивный экспоненциальный
     рост времени повтора (factor) до граничного времени ожидания (border_sleep_time)"""
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            current_sleep_time = start_sleep_time  # на сайте указана t, но я ушел от однобуквенного названия
            for i in range(call_count):
                if current_sleep_time < border_sleep_time:
                    sleep(current_sleep_time)
                    print(f"Запуск номер {i + 1}. "
                          f"Ожидание: {current_sleep_time} секунд. "
                          f"Результат декорируемой функций = {result}")
                    current_sleep_time = round(current_sleep_time * 2 ** factor, 2)
                else:
                    sleep(border_sleep_time)
                    print(f"Запуск номер {i + 1}. "
                          f"Ожидание: {border_sleep_time} секунд. "
                          f"Результат декорируемой функций = {result}")
            print("Конец работы")
            return
        return wrapper
    return real_decorator


@my_decorator(call_count=7, start_sleep_time=1, factor=1.1, border_sleep_time=10)
def testing_func(number: int) -> int:
    return number * 2


if __name__ == "__main__":
    testing_func(5)
