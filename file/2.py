from functools import wraps

def validate(*conditions):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, condition) in enumerate(zip(args, conditions)):
               if not condition(arg):
                    raise ValueError(f"Значение: {arg} не соответствует условию")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate(lambda x: x > 0, lambda y: isinstance(y, str))
def my_function(x, y):
    pass

print(my_function(5, '5'))
