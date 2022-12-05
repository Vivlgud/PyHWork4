# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def find_simple_mult(number:int)->list:
    """Находит простые множители числа и выводит их в список
    
    Args:
        int - натуральное число
    Returns:
        list - список простых множителей
    """
    list_res = []
    number = abs(number)
    if number<2:
        return print('Введите число больше 2')
    else:   
        for i in range(2, number+1):
            if number % i == 0:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    list_res.append(i)
        return list_res


while True:
    flag='q'
    num = input("Введите целое число или 'q' для выхода из программы: ")
    if num in flag:
        exit()
    else:
        list=find_simple_mult(int(num))
        print(f'Простые множители числа {num} - {list}')




