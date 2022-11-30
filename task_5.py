import time
# Составьте алгоритм нахождения случайного числа без использования библиотеки random.

time_report = time.time()
random_number = str(time_report)

try:
    num1 = abs(int(input('Вывод случайного числа. Диапазон: от 1-го до 5-ти значного числа. Введите число: \n')))
    if num1 == 1:
        print (random_number[11:12])
    elif num1 == 2:
        print (random_number[11:13])
    elif num1 == 3:
        print (random_number[11:14])
    elif num1 == 4:
        print (random_number[11:15])
    elif num1 == 5:
        print (random_number[11:16])
    elif num1 < 1 or num1 > 5:
        print('Диапазон вывода числа: от 1-го до 5-ти значного числа')

except ValueError:
    print('Попробуйте заново. Нужно ввести цифру от 1 до 5')

