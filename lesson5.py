def sum_ignore_non_numbers(items):
    summa = 0
    for i in items:
        if type(i)==int or type(i)==float:
           summa += i
        else:
            summa +=0
    return summa

sum_ignore_non_numbers(["LLLLL"," ", 'Hey', None, ";;ll"])

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
#print(is_triangle(3, 4, 5))

def average(*args):
    total = 0
    count = 0
    for a in args:
        total += a
        count += 1
        aver = total / count
    return aver
   # print(aver)

average(1,2,3,4,5,6,7,8)

# def average(*args):
#     if not args:
#         return 0
#     return sum(args) / len(args)

#print(average())

fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry', 'Mango']
fruits_2 = ['Mango', 'apple', 'orange', 'cherry']

def common_strings(list1, list2, ignore_case=True):
    list3 = []
    if ignore_case:
        list1 = [item.lower() for item in list1]
        list2 = [item.lower() for item in list2]
    return [item.lower() for item in list1 if item in list2]

# print(common_strings(fruits_1, fruits_2))

