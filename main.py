# Какие типы данных есть в python? И какие изменяемые и неизменяемые  ?

int 
str 
float
bool
##########
dict
set 
############################################################

# Принципы ООП 

# ООП - Объекино ориентированная программирования 

# Наследование
# Инкапсуляция
# Палимарфизм
# Абстракция
############################################################


# Что такое inline кнопки в aiogram ?

# сами напишите  
############################################################


# Что такое Django ORM ? 

# Это обработсчик базы данных, 

# он переводит наш models.py на язык SQL

############################################################

# С помощью какой технологии делается автодокументация DRF ?

# swagger 

# redoc
####################################################

# в чем отличие aiogram от других библеотек ?


# aiogram являетя ассинхронной библеотекой 
#####################################################


# 200 http код, что она озночает ?

# все ок 


# Что такое класс models.Model в django от которого мы наследуемся

# это абстракный класс в django от которого мы наследуемся 
####################################################################


# За что отвечает папки templates и static в django проекте ?

# templates - html 

# static - ccs, js, fonts, img, 

##################################################################

# что такое синхронность и ассинхронность ? 

# (aiogram.png)

####################################################################

# На каком паттерне проектирования построен Django?

# MVT, или Model-View-Template

#############################################################

# Назовите основные https запросы

# get 

# post 

# put 

# patch 

# delete



# 1) Напишите функцию, которая принимает список, из списка выдает случайное
# значение из списка и записывает результат в txt файл. Список language =
# ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
# 2) У нас есть переменная text которая, хранит в себе текст:
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum.
# Откройте файл text.txt и запишите текст в файл 2 способами
# ДОП ЗАДАЧА:
# 3) Написать программу, которая откроет созданный в задаче 2 файл text.txt,
# скопирует весь текст и запишет его в новый файл wikipedia.txt .

# 4) Создайте модуль с двумя функциями, которые вычисляли бы периметр и
# площадь прямоугольника. Подключите этот модуль к основной программе и
# вызовите эти функции с аргументами.
# 5) У нас есть список lst = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]. Написать функцию которая
# переворачивает список. И используйте эту функцию на другом файле
# 6) Написать функцию, которая принимает hour(час), min(минуту), sec(секунды). И
# вам нужно превратить их в секунды. Вызовите его на другом файле






#геттеры и сеттеры в python ?

#Python, которые позволяют получать и устанавливать значения атрибутов объекта. 
#Геттеры используются для получения значения атрибута, 
#а сеттеры - для установки значения атрибута.

#################################################################################################
# Что такое декораторы 
# Декораторы в Python - это специальные функции, которые позволяют изменять\
# поведение других функций или методов. 
# Они используются для добавления дополнительной функциональности к существующему коду без его изменения
 


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()
####################################################################################

# что такое JWT token ?

# accses token = 

# refresh token =




# Задача об обработке списка: 
# Напишите функцию на Python, которая принимает список чисел и возвращает новый список, содержащий только уникальные числа из исходного списка в том же порядке. Например, для списка [1, 2, 5, 2, 3, 1, 4, 5] ваша функция должна вернуть список [1, 2, 5, 3, 4].

# Задача "Конвертер Температуры": 
# Напишите функцию convert_temperature, которая принимает два аргумента: число (температура) и строку (единица измерения: 'C' для Цельсия, 'F' для Фаренгейта). Функция должна конвертировать температуру из Цельсия в Фаренгейты и наоборот. Формулы конвертации: C = (F - 32) * 5/9 и F = C * 9/5 + 32.

# Задача "Поиск Слова в Тексте": 
# Напишите функцию find_word, которая принимает два аргумента: текст (строка) и слово (строка), и возвращает количество раз, которое это слово встречается в тексте. Учтите, что поиск должен быть нечувствителен к регистру. Например, find_word("Hello world, hello Python", "hello") должна возвращать 2.

def numbers(input_list):
    list = []
    seen = set()

    for num in input_list:
        if num not in seen:
            list.append(num)
            seen.add(num)

    return list


input_list = [1, 2, 5, 2, 3, 1, 4, 5]
result = numbers(input_list)
print(result)



def find_word(text, word):
    text_lower = text.lower()
    word_lower = word.lower()


    count = text_lower.count(word_lower)

    return count


text = "Hello world, hello Python"
word = "hello"
result = find_word(text, word)
print(result)  
