# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

#a = int(input("Введите число: "))
#st = ''

# while a > 0:
#    ost = a % 2
#    st = str(ost) + st
#    a = a // 2

# print(st)


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#lst = [2, 3, 5, 9, 3]
#l = len(lst)
#sum_ofel = 0

#for i in range(l):
#    if i % 2 == 1:
#        sum_ofel = sum_ofel + lst[i]

#print(sum_ofel)



#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#my_lst = [1.1, 1.2, 3.1, 5, 10.01]

#min_el = 1
#max_el = 0

#for i in my_lst:
#    if (i - float(i)) <= min_el:
#        min_el = i - float(i)

#print(min_el)      
#if (i - float(i)) >= max_el:
#        max = i - float(i)

#print(max_el - min_el)



#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

#my_lst = [2, 3, 5, 6]
#nums = []

#for i in range((len(my_lst)+1) //2):
#        nums.append(my_lst[i] * my_lst[len(my_lst)-1 - i])
#print(nums)        


#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input('Введите число: ')) 
k1 = 0
k2 = 1
if k <= 0:
    k = input('Введите число > 0: ')
elif k == 1:
    print(k1)
elif k == 2:
    print(k2)
else:
    print(0, 1, end=' ')
    for i in range(2, k):
        k1, k2 = k2, k1 + k2
        print(k2, end=' ')


#не знаю как вывести отрицателные индексы