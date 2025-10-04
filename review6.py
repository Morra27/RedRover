#Используя функцию map()  и lambda преобразуйте список чисел в список их кубов.

# numbers = [-1, 0, 1, 3, 0.33333]
# cube = map(lambda x: x**3, numbers)
# print(list(cube))

# Дан список цифр. Используя filter() и lambda оставьте только положительные числа в списке.

# numbers = [-1, 0, 1, 2, 4, 6, -3, 0.33333]
# positive = filter(lambda x: x > 0, numbers)
# print(list(positive))

# Создайте файл my_math с функциями сложения, вычитания, деления и умножения. В основном файле импортируйте модуль и используйте эти функции.


# import my_math
# numbers = [2, 5]
# print(my_math.summ(*numbers))
# print(my_math.div(5, 10))
# print(my_math.sub(5, 10))
# print(my_math.mul(6, 10))

# Напишите файл converter, где будут функции, переводящие температуру в градусы цельсия и градусы фаренгейта. Вызовите эти функции в основном файле. Формулы перевода F = 9/5  C + 32, С =5/9 (F - 32)

# from converter import *
# print(f_to_c(451))
# print(c_to_f(32))

# Дан список слов. С помощью filter() и lambda  оставьте в списке только те слова, длина которых больше 3.

# list1 = ["apple", "dog", "house", "book", "car", "sun", "вода", "дерево", "компьютер", "сон"]
# letter3 = filter(lambda x: len(x) == 3, list1)
# print(list(letter3))
