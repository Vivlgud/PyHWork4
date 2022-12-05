# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, 
# которые имеют средний балл более «4».
# Нужно перезаписать файл.


with open('log_names.txt') as file:
    log_names = file.read().rstrip().split('\n')



with open('log_names.txt','w') as file:
    
    for i in log_names:
        str_temp=i.rsplit(' ', 1)
        if int(str_temp[1])>4:
            str_temp[0]=str(str_temp[0]).upper()
        str_temp=str(str_temp)
        str_temp=str_temp.replace("'"," ")
        str_temp=str_temp.replace(","," ")
        str_temp=str_temp.replace("    "," ")
        file.write(f'{str_temp[2:-2]} \n')
        
    


   




