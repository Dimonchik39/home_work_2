import random
# Дан массив размера N. После каждого отрицательного 
# элемента массива вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

array = []
try:
    number = int(input('Введите размерность массива: \n'))
    for i in range(number):
        arr = random.randint(-100,100)
        array.append(arr)
    print(array)

    for i in range(len(array)-1, -1, -1):
        if array[i] < 0:
            array.insert(i+1, 0)
    print(array)

except ValueError:
    print('Попробуйте заново ввести целое число')   