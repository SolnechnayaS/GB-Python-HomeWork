Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
in
Number of words: 10
out
авб абв бав абв вба бав вба абв абв абв
авб бав вба бав вба
in
Number of words: 6
out
ваб вба абв ваб бва абв
ваб вба ваб бва
in
Number of words: -1
out
The data is incorrect

2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
Алгоритм RLE
in
Enter the name of the file with the text:
'text_words.txt'
Enter the file name to record:
'text_code_words.txt'
Enter the name of the file to decode:
'text_code_words.txt'
out
aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
out in file
'text_words.txt'
aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
vbbwwPPuuuTTYyWWQQ
'text_code_words.txt'
5a29v4s3D3d2F4g2O3i2a1
1v2b2w2P3u2T1Y1y2W2Q

* 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.
Эмодзи

** 4. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
Добавьте игру против бота, можно не добвлять
Подумайте как наделить бота "интеллектом"
Стратегии выигрыша