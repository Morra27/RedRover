#1
# def solution(string):
#     str1 = ""
#     for char in string:
#         str1 = char + str1
#     return str1
#
# print(solution("Aloha"))

def square_sum(numbers):
    squared_sum = 0
    for i in numbers:
        squared_sum += i**2
    return squared_sum
print(square_sum([1, 2, 2]))
