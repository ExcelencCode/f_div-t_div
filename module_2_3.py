my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0                     # Создаем счётчик для перебора списка
while x < len(my_list):   # задаём условие.
    if my_list[x] > 0:    # Если число положительное,
        print(my_list[x]) # выводим его на экран
        x += 1            # и переходим к следующему элементу
    elif my_list[x] == 0:   # Если встречается ноль
        x += 1
        continue          # пропускаем его и возвращаемся к началу цикла
    else:                 # Иначе
        break             # прерываем цикл