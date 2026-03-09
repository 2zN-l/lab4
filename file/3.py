from functools import wraps

def validate(*conditions):
    def decorator(func):
        def wrapper(*args):
            if len(args) < len(conditions):
                raise ValueError("Мало аргументов")
            for i, (arg, condition) in enumerate(zip(args, conditions)):
                if not condition(arg):
                    raise ValueError(f"Аргумент '{arg}' не удовлетворяет условию")
            return func(*args)
        return wrapper
    return decorator

def collection(stop_value='stop'):
    collected_args = []
    
    def inner(x):
        nonlocal collected_args
        
        if x == stop_value:
            result = collected_args.copy()
            collected_args.clear()
            return result
        
        return validated_inner(x)
    
    @validate(lambda x: x > 0)
    def validated_inner(x):
        nonlocal collected_args
        collected_args.append(x)
        return f"ДОБАВЛЕНО: {x}"
    
    return inner


collector1 = collection('stop')

print(collector1(5))   
print(collector1(10))   
print(collector1(3))      

try:
    print(collector1(-5))
except ValueError as e:
    print(f"Ошибка: {e}")

print(collector1('stop')) 