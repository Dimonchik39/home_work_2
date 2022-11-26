# Напишите программу, которая принимает на вход число N и выдает 
# набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

try:
    number = int(input('Введите целое число: \n'))
    print('Число введено верно')

    list_result = []
    temp = 1
    for i in range(1, number + 1):
        temp = temp * i
        list_result.append(temp)
        print(list_result)

except ValueError:
    print('Попробуйте заново ввести целое число')