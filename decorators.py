from unittest import result

"""
    Позволяют изменять поведение функций или методов без изменения их исходного кода. 
    Они действуют как обертки, добавляя дополнительную функциональность к существующему коду.
    
    Примеры использования декораторов:

    - Логирование: Добавлять записи в лог перед или после выполнения функции.
    - Проверка типов: Проверять типы аргументов, передаваемых в функцию.
    - Кэширование: Кэшировать результаты вызова функции для ускорения последующих вызовов.
    - Декораторы свойств: Создавать свойства классов.
    - Синхронизация: Обеспечивать синхронный доступ к ресурсам в многопоточных приложениях.
"""

def decorator_function(original_fn):
    def wrapper(*args, **kwargs):
        # Some action before
        print("Some action before")

        result = original_fn(*args, **kwargs)

        # Some action after
        print("Some action after")
        return result
    return wrapper


@decorator_function
def my_function(a, b):
    print("This is my function")
    return (a, b)

# result = my_function(100, 50)
# print(result)


def log_func(fn):
    def wrapper(*args, **kwargs):
        print("This is log function")
        print(F"Function name is {fn.__name__}")
        print(F"Function args is {args}, kwargs is {kwargs}")
        result = fn(*args, **kwargs)
        print(f"Function result is {result}")
        return result
    return wrapper


@log_func
def mult(a, b):
    return a * b


# print(mult(4, 50))

test = {
    'a': 10,
    'b': 20
}

@log_func
def sum(a, b):
    return a + b

# print(sum(a=10, b=50)) # should be named
# print(sum(test)) # like args


def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Argument {arg} is not a number")

        return fn(*args, **kwargs)
    return wrapper


@validate_args
def sum_nums(a, b):
    return a + b

# try:
#     print(sum_nums(7, 2))
#     print(sum_nums(10.5, 7.2))
#     print(sum_nums(10.5, '7.2'))
# except ValueError as e:
#     print(e)


def is_user_auth():
    return True


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_auth():
            print("User auth was successful")
            return fn(*args, **kwargs)
        else:
            raise Exception("User auth was NOT successful")
    return wrapper


@check_user_auth
def do_smth():
    print("Do smth")

# try:
#     do_smth()
# except Exception as e:
#     print(e)

def repeat(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def repeat3(name):
    print(f"Hello {name}")

# repeat3('Seva')


class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before function call")
        result = self.func(*args, **kwargs)
        print("After function call")
        return result

@MyDecorator
def my_function():
    print("Inside my_function")

# my_function()

class LogCalls:
    def __init__(self, cls):
        self.cls = cls
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"Calling {self.cls.__name__} (call #{self.call_count})")
        obj = self.cls(*args, **kwargs)
        print(f"{self.cls.__name__} object created.")
        return obj

@LogCalls
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def some_method(self):
        return self.x + self.y

# Create an instance of the class
obj = MyClass(2, 3)

# print(obj.some_method())
