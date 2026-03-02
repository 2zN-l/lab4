from functools import wraps

def validate(*conditions):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) < len(conditions):
                raise ValueError("Мало аргументов")
            for i, (arg, condition) in enumerate(zip(args, conditions)):
                if not condition(arg):
                    raise ValueError(f"Аргумент '{arg}' не удовлетворяет условию")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def collection(stop_value=None):
    collected_args = []
    

    @validate(lambda x: (isinstance(x, int) and x > 0) or x == stop_value)
    def inner(arg):
        nonlocal collected_args
    
        if arg == stop_value:
            result = collected_args.copy()
            collected_args.clear()
            return result
        else:
            collected_args.append(arg)
            return f"ДОБАВЛЕНО: {arg}"
    
    return inner

