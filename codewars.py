#1
# def solution(string):
#     str1 = ""
#     for char in string:
#         str1 = char + str1
#     return str1
#
# print(solution("Aloha"))

#2
# def square_sum(numbers):
#     squared_sum = 0
#     for i in numbers:
#         squared_sum += i**2
#     return squared_sum
# print(square_sum([1, 2, 2]))

'''
In this simple exercise, you will write a function that takes two integers; n and limit; and returns a list of the multiples of n up to and possibly including limit.
It is guaranteed that n > 0 and limit >= n.
For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.
'''

# def find_multiples(integer, limit):
#     list1 = []
#     mu = limit // integer
#     for i in range(1, mu+1):
#         list1.append((integer*i))
#     #return list1
#     print(list1)
#
# find_multiples(1, 27)

'''
Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').
Create a function which translates a given DNA string into RNA.
'''

# def dna_to_rna(dna):
#     rna = ''
#     for char in dna:
#         if char == 'T':
#             rna += 'U'
#         else:
#             rna += char
#     return rna
#
# dna_to_rna('TTAGAGCACT')