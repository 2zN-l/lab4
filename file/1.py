def colection(stop_value=None):
    collected_args = []
    
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

a = colection(stop_value='stop')

print(a(1)) 
print(a(2)) 
print(a(3)) 
print(a('stop')) 
print(a(4))
print(a(5))     
print(a('stop'))