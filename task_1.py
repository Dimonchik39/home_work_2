# 1 - Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11

# number = input('Введите вещественное число: \n')
# summ = 0
# for digit in number:
#     if digit.isdigit():
#         summ += int(digit)
# print(summ)



try:
    number = abs(float(input('Введите вещественное число: \n')))
    print('Число введено верно')

    str_number = str(number)
    str_number = str_number.replace('.', '')
    int_str = list(str_number)
    int_num = map(int, int_str)
    summ = sum(int_num)
    print(f'Сумма цифр: {summ}')

except ValueError:
    print('Попробуйте заново ввести число')