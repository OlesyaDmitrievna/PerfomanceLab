def find_circular_path(n, m):
    circular_array = list(range(1, n+1))  # Создаем круговой массив
    current_index = 0  # Индекс текущего элемента
    next_index = 3 #Индекс элемента для следующего среза
    path = []  # Массив для хранения пути

    while circular_array[next_index]!=1:  # Пока снова не вернемся к 1 элементу
        next_index = (current_index + m - 1) % n  # Индекс следующего элемента
        path.append(circular_array[current_index])  # Добавляем текущий элемент в путь
        current_index = next_index  # Обновляем индекс текущего элемента

    return path
def cut_numbers(input_str):
    numbers = input_str.split()  # Разделение введенной строки по пробелу

    # Теперь у нас есть список строк, представляющих введенные числа
    # Преобразуем их в числа
    if len(numbers) == 2:
        num1 = int(numbers[0])  # Преобразование первой строки в число
        num2 = int(numbers[1])  # Преобразование второй строки в число
        return num1, num2

input_str = input('Введите n и m для кругового массива:') # Задаем значение n (размер кругового массива) и m (интервал движения) через пробел
n, m = cut_numbers(input_str)
circular_path = find_circular_path(n, m)
path = ''.join(map(str, circular_path))
print(path)