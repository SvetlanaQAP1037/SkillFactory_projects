sequence = []

while True:
    try:
        sequence = list(map(float, (input("Введите последовательность чисел через пробел: ").split())))

    except ValueError:
        print("Неправильный формат чисел!")
    else:
        print("Спасибо, числа введены корректно!")
        break

while True:
    try:
        number = float(input("Введите число, отличное от введенных ранее: "))
    except ValueError:
        print("Неправильный формат числа!")
    else:
        sequence.append(number)
        print("Спасибо, что ввели число!")
        break
print('Введённая последовательность чисел', sequence)

def binary_search(sequence: list, number):
    left, right = 0, len(sequence)
    if number == sequence[-1]:
        print('Число не соответствует всем заданным условиям: в последовательности нет числа, больше введенного!')

    while left < right:
        middle = (left + right) // 2
        if sequence[middle] < number:
            left = middle + 1
        else:
            right = middle
    return left - 1

def insertion_sort():
    for i in range(0, len(sequence)):
        x = sequence[i]
        idx = i
        while idx > 0 and sequence[idx-1] > x:
            sequence[idx] = sequence[idx-1]
            idx -= 1
            sequence[idx] = x
    return sequence

print('Сортировка списка по возрастанию элементов: ', insertion_sort())
print("Номер позиции элемента, меньшей позиции введенного пользователем числа: ", binary_search(sequence, number))