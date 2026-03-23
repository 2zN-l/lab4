
class Validate:
    
    def __init__(self, *conditions):
        self.conditions = conditions
        self.default_condition = lambda x: x > 0
    
    def __call__(self, func):
        def wrapper(*args):
            # Определяем условия для проверки
            check_conditions = self.conditions
            if not check_conditions:
                check_conditions = (self.default_condition,)
            
            if len(args) < len(check_conditions):
                raise ValueError(f"Мало аргументов. Нужно {len(check_conditions)}")
            
            for i, (arg, cond) in enumerate(zip(args, check_conditions)):
                if not cond(arg):
                    raise ValueError(f"Аргумент '{arg}' не удовлетворяет условию")
            
            return func(*args)
        return wrapper


# ====================== С УСЛОВИЕМ ======================

def collection(stop_value='stop'):
    collected_args = []
    
    @Validate(lambda x: x > 5)
    class Collector:
        def __init__(self, x):
            self.x = x
        
        def add(self):
            collected_args.append(self.x)
            return f"ДОБАВЛЕНО: {self.x}"
    
    def inner(x):
        if x == stop_value:
            result = collected_args.copy()
            collected_args.clear()
            return result
        
        collector = Collector(x)
        return collector.add()
    
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
print(collector1('stop'))   # [10, 22]
print()


# ====================== БЕЗ УСЛОВИЯ ======================

def collection(stop_value='stop'):
    collected_args = []
    
    @Validate()
    class Collector:
        def __init__(self, x):
            self.x = x
        
        def add(self):
            collected_args.append(self.x)
            return f"ДОБАВЛЕНО: {self.x}"
    
    def inner(x):
        if x == stop_value:
            result = collected_args.copy()
            collected_args.clear()
            return result
        
        collector = Collector(x)
        return collector.add()
    
    return inner

collect = collection()

print(collect(10))
try:
    print(collect(-5))
except ValueError as e:
    print(f"Ошибка: {e}")
print(collect('stop'))  # [10]
print()


# ====================== РЕКУРСИЯ ======================

@Validate(lambda x: x >= 0)
class FactorialCalculator:
    def __init__(self, n):
        self.n = n
    
    def calculate(self):
        return self._factorial(self.n)
    
    def _factorial(self, n):
        if n == 0:
            return 1
        return n * self._factorial(n - 1)

def factorial(n):
    calculator = FactorialCalculator(n)
    return calculator.calculate()

print(factorial(5))  # 120
try:
    print(factorial(-3))
except ValueError as e:
    print(f"Ошибка: {e}")