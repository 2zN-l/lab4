def validate(condition=None):
    def decorator(func):
        def wrapper(x):
            if condition is None:
                cond = lambda x: x > 0
            else:
                cond = condition
            
            if not cond(x):
                raise ValueError(f"{x} не подходит условию")
            return func(x)
        return wrapper
    return decorator

#====================== С УСЛОВИЕМ =============================

def collection(stop_value='stop'):
    collected_args = []
    
    def inner(x):
        nonlocal collected_args
        
        if x == stop_value:
            result = collected_args.copy()
            collected_args.clear()
            return result
        
        return validated_inner(x)
    
    @validate(lambda x: x > 5)
    def validated_inner(x):
        nonlocal collected_args
        collected_args.append(x)
        return f"ДОБАВЛЕНО: {x}"
    
    return inner

collector1 = collection('stop')

  
print(collector1(10))   
print(collector1(22))      
try:
    print(collector1(5))
except ValueError as e:
    print(f"Ошибка: {e}")
try:
    print(collector1(-5))
except ValueError as e:
    print(f"Ошибка: {e}")

print(collector1('stop')) 


#============================ БЕЗ УСЛОВИЯ ==============================

def collection(stop_value='stop'):
    collected_args = []
    
    def inner(x):
        nonlocal collected_args
        
        if x == stop_value:
            result = collected_args.copy()
            collected_args.clear()
            return result
        
        return validated_inner(x)
    
    @validate
    def validated_inner(x):
        nonlocal collected_args
        collected_args.append(x)
        return f"ДОБАВЛЕНО: {x}"
    
    return inner

collect = collection()
print(collect(10))
try:
    print(collector1(-5))
except ValueError as e:
    print(f"Ошибка: {e}")
print(collect('stop'))

#======================== РЕКУРСИЯ =========================

@validate(lambda x: x >= 0)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
print(factorial(0))