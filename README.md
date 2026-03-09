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

1. Создан декоратор validate – проверяет аргументы функции на соответствие заданным условиям
2. Создано замыкание collection – накапливает аргументы в коллекции до получения стоп-слова
4. Применен декоратор к замыканию. Сначала внутренняя функция проверяет аргумент на стоп-слово
5. Если это стоп-слово – возвращает накопленное и очищает коллекцию
6. Если обычный аргумент – передает в декорированную функцию для валидации и добавления




``` python

collector1 = collection('stop')

print(collector1(5))   
print(collector1(10))   
print(collector1(3))      

try:
    print(collector1(-5))
except ValueError as e:
    print(f"Ошибка: {e}")

print(collector1('stop')) 

```
<img width="825" height="158" alt="image" src="https://github.com/user-attachments/assets/89788165-f7d5-47a9-9a5d-b51286359703" />



# Список использованной литературы
1. [Декораторы Python: пошаговое руководство](https://habr.com/ru/companies/otus/articles/727590/)
2. [Коллекции Python](https://university.ylab.io/articles/tpost/tinb2nne31-kollektsii-python)
3. [Валидируйте это немедленно](https://habr.com/ru/articles/800837/)

