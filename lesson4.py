# Сгенерируйте список numbers, состоящий из чисел в диапазоне от 0 до 100 включительно, которые делятся без остатка как на 2, так и на 3.
# Выведите список numbers на экран.

# numbers1 = [d for d in range(100) if d % 3 == 0]
# numbers2 = [c for c in numbers1 if c % 2 == 0]
# print(numbers2)

# numbers = []
# for a in range(100):
#     if a % 2 == 0:
#         if a % 3 ==0:
#             numbers.append(a)
#
# print(numbers)

# Имеется список items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# Составьте новый список numbers, который содержит только целые числа (int) и вещественные числа (float) из списка items.
# Выведите на экран сумму чисел в numbers.

# numbers = []
# items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# for item in items:
#     if type(item) is int:
#         numbers.append(item)
#     elif type(item) is float:
#         numbers.append(item)
# print(numbers)
# sum = sum(numbers)
# print(sum)

# Создать список messages, который будет хранить “сообщения”.
# Программа должна в бесконечном цикле запрашивать у пользователя ввести сообщение (строку) с клавиатуры и сохранять ее в список messages. Причем программа должна запоминать не более 5 последних сообщений. То есть, если длина списка messages превысила 5, то первое сообщение в нем должно быть удалено.
# Если пользователь ввел “Пока”, то программа должна вывести “Ну ладно, пока!” и список последних сообщения на экран.


# messages = []
# while True:
#     message = input("Enter messages: ")
#     if message == "Пока":
#         break
#     messages.append(message)
#     if len(messages) > 5:
#         messages.pop(0)
# print(messages)


# products = {
#      "apple": {"quantity": 10, "price": 100},
#     "banana": {"quantity": 20, "price": 50},
#     "orange": {"quantity": 15, "price": 80},
#     "grape": {"quantity": 8, "price": 120},
#     "milk":{"quantity": 12, "price": 90},
#      "bread": {"quantity": 30, "price": 40}
# }
# for key in products.values():
#     key["price"] = key["price"] * 1.2
# print(products)
#
# del products["milk"]
#
# products["salt"] = {"quantity": 7, "price": 12}
# print(products)
#
# cost = 0
# for key in products.values():
#     cost += key["price"] * key["quantity"]
# print(cost)



# keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']
# values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]
#
# info = dict(zip(keys, values))
# print(info)


str = '2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя'
cipher = {
    "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
    "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
    "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
    "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
    "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
}
str2 = ""
for char in str:
    if char in cipher.keys():
        str2 += cipher[char]
print(str2)

