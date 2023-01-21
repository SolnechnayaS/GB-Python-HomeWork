import os
clear = lambda: os.system('clear')
clear()

print("Задача 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.")
n = int(input("Введите целое число: "))
print(list([x for x in range(20,n+1) if (not x%20 or not x%21)]))