# n = float(input("Введите число: "))
# if n % 2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное")


# day = input("Какой сегодня день? " ).lower()
# if day == "суббота" or day == "воскресенье":
#     print("Сегодня выходной!")
# elif day == "среда":
#     print("Мне сегодня к стоматологу в 15:30")
# elif day in ["понедельник", "вторник", "четверг", "пятница"]:
#     print("Сегодня обычный день")
# else:
#     print("Это не день недели")

# n = int(input("Введите число повторений "))
# text = (input("Введите текст "))
# for _ in range(n):
#     print(text)

# n = int(input("Введите число повторений "))
# text = (input("Введите текст "))
# while True:
#     print(text)
#     n = n - 1
#     if n == 0:
#         break

message = (input("Введите текст ")).lower()
count = 0
for с in message:
    if с in ["а", "о", "у", "и", "ы", "э", "е", "ё", "ю", "я"]:
        count += 1
print(count)

# n = int(input("Введите целое число: "))
# s = 0 + n
# while True:
#     n = int(input("Введите целое число: "))
#     if n < 0:
#         break
#     s += n
# print(s)
