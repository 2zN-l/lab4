from functools import wraps

def validate(*conditions):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if len(args) < len(conditions):
                raise ValueError("Мало аргументов")
            for i, (arg, condition) in enumerate(zip(args, conditions)):
                if not condition(arg):
                    raise ValueError(f"Аргумент '{arg}' не удовлетворяет условию")
            return func(*args)
        return wrapper
    return decorator


@validate(lambda x: x > 0, lambda y: isinstance(y, str))
def my_function(x, y):
     pass

my_function(52, "hello")
try:
    my_function(-5, "hello")
except ValueError as e:
    print(e)

try:
    my_function(10, 123)
except ValueError as e:
    print(e)

try:
    my_function(5)
except ValueError as e:
    print(e)