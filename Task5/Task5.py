# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol
# Первая функция - текст зашифровывает
# Вторая - расшифровывает
# Две промежуточные - считывают с файла и записывают в файл

def read_file(filename:str):
    """ считывает файл
    
    Args: путь к файлу
    Returns: данные из файла
    """
    with open(filename) as file:
        txt=file.read()
    return txt

txt=read_file("text1.txt")


print(txt)
pusto=' '
list = []
count = 1
check = txt[0]
for i in txt[1:]:
    if i != check:
        list.append(count)
        if count >= 1:
            list.append(check)
        check = i
        count = 1
    else:
        count+=1

print(*list, sep='')


