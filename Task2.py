# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

from typing import List


def generate_list(num: int) -> int:

    """Генерирует сортированный список чисел
        
        Args:
            int - натуральное число (количество элементов списка)
        Returns:
            list - список чисел от 1 до 10
    """
    import random
    list_res=[]
    
    for i in range(num):
        list_res.append(int(random.randint(1, 10)))
        list_res.sort()
    return list_res

def delete_repeated_elements(list:List)->list:
    """Убирает повторяющиеся элементы из списка
    
    Args:
        list - список  
    Returns:
        list - список без повторов    

    """
    list_new=[]
    check=list[0]
    list_new.append(check)
    for i in list:
        if check!=i:
            list_new.append(i)
            check=i
    return list_new

while True:
    flag='q'
    number = input("Введите целое число или 'q' для выхода из программы: ")
    if number in flag:
        exit()
    else:
        list=generate_list(int(number))
        print(list)
        
        result=delete_repeated_elements(list)
        print(result)
