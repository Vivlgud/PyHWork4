# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


filename='alphabet.txt'
with open(filename, mode='r',encoding='utf-8') as file:
    dict_alfa=file.readline()
# print(dict_alfa)

def coding_phrase():
    """ Шифрует фразу
        
    Returns: зашифрованный текст
    """

    phrase=input('Введите фразу для шифрования, используя кириллицу: ')
    
    key=int(input('Введите ключ шифрования: '))
    while key>33:
        key-=33
        
    phrase=phrase.upper()
    index,newindex=0,0
    new_phrase=''
    for i in phrase:
        index=dict_alfa.find(i)
        newindex=index+key
        if i in dict_alfa:
            new_phrase+=dict_alfa[index+key]
        else:
            new_phrase+=i
    new_phrase=new_phrase.lower()
    return new_phrase

def write_file(code:str):
    """ Запись зашифрованной фразы в файл coding.txt
        
    Returns: файл с зашифрованным текстом
    """
    filename1='coding.txt'
    with open(filename1, mode='w',encoding='utf-8') as file:
        file.write(code)

write_file(coding_phrase())

def decoding_phrase():
    """ Расшифровывает фразу по ключу
        
    Returns: расшифрованный текст
    """
    key=int(input('Введите ключ шифрования: '))
    while key>33:
        key-=33

    with open("coding.txt", mode='r', encoding='utf-8') as file:
        phrase=file.readline()

    phrase=phrase.upper()
    index,newindex=0,0
    new_phrase=''
    for i in phrase:
        index=dict_alfa.find(i)
        newindex=index-key
        if i in dict_alfa:
            new_phrase+=dict_alfa[index-key]
        else:
            new_phrase+=i
    new_phrase=new_phrase.lower()
    return new_phrase

print(decoding_phrase())





