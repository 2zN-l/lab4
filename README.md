# Задание 1
Замыкание для накопления всех аргументов в коллекции, при получении определённого значения - возврат и очистка коллекции.
1. Внешняя функция colection(stop_value=None) создаёт замыкание и инициализирует пустой список collected_args
2. Внутренняя функция inner(arg) получает аргумент для обработки и через nonlocal получает доступ к списку
3. Если arg равен stop_value, создаётся копия накопленного списка, оригинал очищается, возвращается копия
4. Если arg не равен stop_value, значение добавляется в список
5. Внешняя функция возвращает внутреннюю
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

1. Функция, которая проверяет аргументы
2. Задаём правила проверки
3. Перед запуском функции проверяются все её аргументы
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


# Задание 3
Примените декоратор к замыканию.

1. coll принимает stop_value и условия, возвращает collector
2. Аргументы добавляются в collected, пока не встретится stop_value.
3. Каждый аргумент проверяется условиями.
4. При stop_value возвращается копия collected, затем список очищается.



``` python
c = coll('stop', lambda x: isinstance(x, int) and x > 0)

c(1)
c(2)
print(c('stop'))

```
<img width="184" height="46" alt="image" src="https://github.com/user-attachments/assets/71392b8a-22a0-42c3-9c9a-3965593909d9" />

# Список использованной литературы
1. [Декораторы Python: пошаговое руководство](https://habr.com/ru/companies/otus/articles/727590/)
2. [Коллекции Python](https://university.ylab.io/articles/tpost/tinb2nne31-kollektsii-python)
3. [Валидируйте это немедленно](https://habr.com/ru/articles/800837/)

