def coll(stop_value, *conditions):
    collected = []

    def collector(arg):
        nonlocal collected
        if arg == stop_value:
            result = collected.copy()
            collected.clear()
            return result
        else:
            for condition in conditions:
                if not condition(arg):
                    raise ValueError(f"Аргумент {arg} не удовлетворяет условию ")
            collected.append(arg)
            return None

    return collector


c = coll('stop', lambda x: isinstance(x, int) and x > 0)

c(1)
c(2)
print(c('stop'))