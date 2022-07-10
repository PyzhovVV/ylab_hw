dict_cache = {}


def cache_decorator(func):  # не разобрался в тонкостях type hinting для декоратров
    """Декоратор, кэширующий значения декарируемой функции"""
    def wrapper(number: int, *args, **kwargs):  # не уверен нужны ли тут вообще аргсы и кваргсы
        if number in dict_cache.keys():
            print("кэширование сработало!")
            result = dict_cache[number]
        else:
            result = func(number, *args, **kwargs)
            dict_cache[number] = result
        return result
    return wrapper


@cache_decorator
def multiplier(number: int) -> int:
    return number * 2


if __name__ == "__main__":
    print(multiplier(10))
    print(multiplier(5))
    print(multiplier(16))
    print(multiplier(10))
    print(multiplier(5))
    print(multiplier(3))
