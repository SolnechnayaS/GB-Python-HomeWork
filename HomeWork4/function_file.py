from random import sample
import random
import copy
from decimal import Decimal, getcontext
import function_file


def random_list (len_list):
    new_list = sample (range (1, len_list ** 2), k=len_list)
    return new_list

def random_ratio (len_list):
    temp_list = list(range(-10, 10))+list(range(-10, 10))+list(range(-10, 10))
    new_list = sample (temp_list, k=len_list+1)
    return new_list

def sum_odd (new_list):
    sum=0
    for i in range (len(new_list)):
        if i%2==0:
            sum += new_list[i]
    return sum

def pair_multiplication (new_list):
    list_pair_multiplication = []
    if len(new_list)%2==0:
        for i in range (int(len(new_list)/2)):
            list_pair_multiplication.append (new_list[i]*new_list[-1-i])
    else:
        for i in range (int(len(new_list)/2)+1):
            if i == int(len(new_list)/2):
                list_pair_multiplication.append (new_list[i])
            else:
                list_pair_multiplication.append (new_list[i]*new_list[-1-i])
    return list_pair_multiplication

def binary (number):
    binary_list = []
    while number>0:
        binary_list.insert(0, str(int(number%2)))
        number = int(number/2)
    return binary_list

def random_list_float (len_list):
    list_float = []
    for i in range (len_list):
        list_float.append (round(float(random.random())*10, 2))
    return list_float

def fractional_part (list_float):
    n = len(list_float)
    list_fractional_part = []
    min = float(list_float[0]) - int(list_float[0])
    max = float(list_float[0]) - int(list_float[0])
    
    for i in range (n):
        a = float(list_float[i]) - int(list_float[i])
        list_fractional_part.append(a)
        if a > max:
            max = a
        elif a < min:
            min = a
    print (f'Min: {round(min,2)}, Max: {round(max, 2)}. Difference: {round(max-min,2)}')

def negafibonacci (len_list):
    fib_list = [1,0,1]
    for i in range (3, len_list+2):
        a = fib_list[i-2]+fib_list[i-1]
        fib_list.append (a)
    for i in range (0, len_list-1):
        b = fib_list[1]-fib_list[0]
        fib_list.insert (0, b)
    return fib_list

def prime_factors (number):
    list_prime_factors =[]
    while number>1:
        for i in range (2, number+1):
            if number%i == 0:
                while number%i == 0:
                    list_prime_factors.append (i)
                    number = number/i

    return list_prime_factors

def list_unique_elements (first_list):
    list_unique_elements = list(first_list)
    for i in range (len(first_list)):
        if first_list.count(first_list[i])>1:
            list_unique_elements.remove(first_list[i])

    return list_unique_elements

def decimal_num (number, precision):
    number_dec = number.quantize(Decimal(precision))
    
    return number_dec

def random_polynomial (k, name):
    random_ratio_list = function_file.random_ratio (k)
    temp = random_ratio_list.copy()
    temp.reverse()
    print(f'Коффициенты использумые в многочлене {temp}, сам многочлен записан в файле {name}')
    with open (name, "a", encoding="utf-8") as polynomial:
        polynomial_list = []
        for i in range (2):
            if random_ratio_list[i] ==1:
                if i == 0:
                    polynomial_list.insert(0, f"{random_ratio_list[i]}")
                elif i == 1:
                    polynomial_list.insert(0, f"х")
            elif random_ratio_list[i] !=0:
                if i == 0:
                    polynomial_list.insert(0, f"{random_ratio_list[i]}")
                elif i == 1:
                    polynomial_list.insert(0, f"{random_ratio_list[i]}х")
        for i in range (2, k+1):
            if random_ratio_list[i] == 1:
                polynomial_list.insert(0, f"x^{i}")
            elif random_ratio_list[i] !=0:
                polynomial_list.insert(0, f"{random_ratio_list[i]}x^{i}")
        polynomial.writelines(f'{"+".join(polynomial_list).replace("+-","-")}=0\n')

def temp_name (number):
    match number:
        case 1:
            name = str('poly.txt')
        case 2:
            name = str('poly2.txt')
        case _:
            name = str(input("Введите имя файла для записи: "))
    return name