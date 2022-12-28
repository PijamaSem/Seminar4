# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
nums = input(f'Введите последовательность чисел через пробел ')
# print (type(nums))
# print (nums)
# list_num =[]
list_num = nums.split()
list_dig = []
for i in range(0, len(list_num)):
    if list_num[i].isdigit():
        list_dig.append(list_num[i])
list_dig = list(map(int, list_dig))
set = set(list_dig)
print(set)
