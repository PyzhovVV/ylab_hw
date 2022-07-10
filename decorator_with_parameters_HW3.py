def my_decorator(func):
    """Декоратор"""
    def wrapper(number: int, *args, **kwargs):
        result = func(number)
        return result
    return wrapper


def testing_func():
    ...


if __name__ == "__main__":
    print(testing_func())
    print(testing_func())
    print(testing_func())
