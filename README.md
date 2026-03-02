# Задание 1
Замыкание для накопления всех аргументов в коллекции, при получении определённого значения - возврат и очистка коллекции.
1. Внешняя функция colection(stop_value=None) создаёт замыкание и инициализирует пустой список collected_args
2. Внутренняя функция inner(arg) получает аргумент для обработки и через nonlocal получает доступ к списку
3. Если arg равен stop_value, создаётся копия накопленного списка, оригинал очищается, возвращается копия
4. Если arg не равен stop_value, значение добавляется в список
5. Внешняя функция возвращает внутреннюю, создавая готовый к использованию накопитель
<br>

##### Результат:

``` python
acc = colection(stop_value='stop')

print(acc(1))        # None
print(acc(2))        # None
print(acc(3))        # None
print(acc('stop'))   # [1, 2, 3]
print(acc(4))        # None
print(acc(5))        # None
print(acc('stop'))   # [4, 5]
```


<img width="327" height="169" alt="image" src="https://github.com/user-attachments/assets/bf547dbc-225d-4ef0-bd65-44913ac6d435" />

<br>
<br>
<br>

# Задание 2
Декоратор для валидации аргументов функции с помощью условий:

``` python
@validate(lambda x: x > 0, lambda y: isinstance(y, str))
def my_function(x, y):
    pass
```


##### Результат:

``` python
print(my_function(5, "hello"))
print(my_function(-1, "hello")) 
print(my_function(5, 123))
```

ФОТО НАДА
