# Дан список чисел. Посчитать сколько раз встречается каждое число. Использовать для подсчета функцию
# Подсказка. Для хранения данных использовать словарь. Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in

# 1st method
import random
my_list = [random.randint(0, 10) for i in range(10)]

def count_num(my_list, my_dict):
    """Функция считает кол-во каждого значения и заносит данные в словарь вида
    {key="числа, которые встречаются в списке" : value="кол-во этих чисел в списке"}."""
    for num in my_list:
        if num in my_dict:                                        #  Если итерируемый эл-т списка есть в кач-ве ключа словаря, то увеличиваем значение этого ключа на 1
            my_dict[num] += 1
        else:
            my_dict[num] = 1                                      #  Если итерируемого эл-та списка нет в кач-ве ключа словаря, то добавляем ключ со значением, равным 1

my_dict = {}
count_num(my_list, my_dict)

for num in sorted(my_dict):                                       # sorted() - для вывода содержимого словаря в отсортированном по возрастанию ключей виде
    print(f"The number {num}: appears {my_dict[num]} times in the list {my_list}")



# 2nd method
# import random
# my_list = [random.randint(0, 10) for i in range(10)]

# def count_num(my_list, my_dict = {}):
#     for num in my_list:
#         if my_dict.get(num):                                        
#             my_dict[num] += 1
#         else:
#             my_dict[num] = 1

#     for num in sorted(my_dict):                                                     
#         print(f"The number {num}: appears {my_dict[num]} times in the list {my_list}")                                    

# count_num(my_list)
