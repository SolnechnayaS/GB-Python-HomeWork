import os
clear = lambda: os.system('clear')
clear()
from collections import defaultdict

print("Задача 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.")
list_name = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]

dict_name = defaultdict(list)
for x in range (len(list_name)):
    dict_name[list_name[x][:-(len(list_name[x])-1)]].append(list_name[x])
print(dict(dict_name))