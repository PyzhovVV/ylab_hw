from time import sleep


def my_decorator(func):
    """Декоратор, выполняющий фанкцию (call_count) раз и использующий наивный экспоненциальный
     рост времени повтора (factor) до граничного времени ожидания (border_sleep_time)"""
    def wrapper(*args, **kwargs):
        call_count = int(input("Количество запусков = "))
        start_sleep_time = float(input("Начальное время повтора = "))
        factor = float(input("Во сколько раз нужно увеличить время ожидания = "))
        border_sleep_time = float(input("Граничное время ожидания = "))
        result = func(*args, **kwargs)
        for i in range(call_count):
            if start_sleep_time < border_sleep_time:
                sleep(start_sleep_time)
                print(f"Запуск номер {i + 1}. "
                      f"Ожидание: {start_sleep_time} секунд. "
                      f"Результат декорируемой функций = {result}")
                start_sleep_time = round(start_sleep_time * 2 ** factor, 2)
            else:
                sleep(border_sleep_time)
                print(f"Запуск номер {i + 1}. "
                      f"Ожидание: {border_sleep_time} секунд. "
                      f"Результат декорируемой функций = {result}")
        print("Конец работы")
        return
    return wrapper


@my_decorator
def testing_func(number: int) -> int:
    return number * 2


if __name__ == "__main__":
    testing_func(5)
