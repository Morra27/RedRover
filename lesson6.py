# from lesson5 import sum_ignore_non_numbers
#
# print(sum_ignore_non_numbers(["LLLLL", 1, 5.55, " ", None, 'Hey', ";;ll"]))

# from lesson5 import *
#
# print(sum_ignore_non_numbers(["LLLLL", 1, 5.55, " ", None, 'Hey', ";;ll"]))
#
# print(is_triangle(3, 4, 5))
#
# print(average(1,2,3,4,5,6,7,8))
#
# print(common_strings(['banana', 'APPLE', 'watermelon', 'cherry'], ['banaNa', 'Mango', 'apple', 'orange', 'cherry']))
#
# print(average(1,2,3,4,5,6,7,8))


'''Создайте анонимную функцию pow, которая принимает 2 аргумента x и y.
Функция должна возвращать x, возведенное в степень y.'''

# pow = lambda x, y: x ** y
# print(pow(2, 3))



'''Создайте функцию snake_talk, которая принимает 1 аргумент text (строка).
- Функция должна создать новую строку, где все гласные буквы
aeiouyAEIOUY в строке text дублируются.
- Например, такой вызовы функции snake_talk(“Harry”) должен вернуть
строку “Haaryy”.'''

# def snake_talk(text):
#     text1 = ""
#     for char in text:
#         text1 += char
#         if char in "aeiouyAEIOUY":
#             text1 += char
#     return text1
#
# print(snake_talk("text"))



