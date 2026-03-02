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
a = colection(stop_value='stop')

print(a(1)) 
print(a(2)) 
print(a(3)) 
print(a('stop')) 
print(a(4))
print(a(5))     
print(a('stop'))
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
<br>

1. Написана функция, которая проверяет аргументы других функций
2. Добавлена возможность задавать правила проверки (например: "число должно быть больше 0")
3. Сделано так, что перед запуском функции проверяются все её аргументы
4. Если аргумент не подходит под правило - программа выдаёт ошибку
5. Если всё хорошо - функция работает как обычно

##### Результат:

``` python
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
```

<img width="655" height="68" alt="image" src="https://github.com/user-attachments/assets/ca95015a-df0e-4a3e-b349-74cd3ef1c45f" />


<br>
<br>
<br>

