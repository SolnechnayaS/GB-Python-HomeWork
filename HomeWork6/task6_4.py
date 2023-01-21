import os
clear = lambda: os.system('clear')
clear()
from collections import defaultdict

print("Задача 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.")
list_name = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Юнона Ветрякова", "Борис Аркадьев", "Антон Серов", "Павел Анисимов"]

list_name_sublist = [list_name[i].split(' ') for i in range (len(list_name))]

first_letter_lastname =[]
first_letter_name =[]
for x in range (len(list_name)):
    first_letter_lastname.append(list_name_sublist[x][1][:-(len(list_name_sublist[x][1])-1)])
    first_letter_name.append(list_name_sublist[x][0][:-(len(list_name_sublist[x][0])-1)])


print(list_name)
# print(first_letter_lastname)
# print(first_letter_name)

dict_lastname = defaultdict(list)
for x in range (len(list_name_sublist)):
    dict_lastname[list_name_sublist[x][1][:-(len(list_name_sublist[x][1])-1)]].append(str(list_name_sublist[x][0]+" "+list_name_sublist[x][1]))

print(dict(dict_lastname))