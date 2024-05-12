resolution_1, resolution_2 = map(int, input('Введите через пробел разрешение: ').split())
find = input('Что надо найти?\nКол-во цветов(1)    Размер файла(2)\nВведите цифру вашего запроса: ')
if find == '1':
    size = int(input('Введите размера файла: '))
    measure = int(input('В каких единицах измерения?\nБайт(1)    Килобайт(2)    Мегабайт(3)    Гигабайт(4)\nВведите цифру вашего запроса: '))
    act_size = size*8*1024**(measure-1)
    opacity = int(input('Кол-во БИТ, отведенных на степень прозрачности: '))
    i = act_size / (resolution_1*resolution_2) - opacity
    answer = int(2**i)
    print(answer)
else:
    i = int(input('На вход принимается?\nКол-во цветов(1)    Кол-во БИТ для цвета(2)'))
    amount = int(input('Введите количество: '))
    opacity = int(input('Кол-во БИТ, отведенных на степень прозрачности: '))
    measure = int(input('В каких единицах измерения должен быть записан ответ?\nБайт(1)    Килобайт(2)    Мегабайт(3)    Гигабайт(4)\nВведите цифру вашего запроса: '))
    meas = {1:'Байт', 2:'Килобайт', 3:'Мегабайт', 4:'Гигабайт'}
    if i == 1:
        x = 0
        for k in range(48):
            if 2 ** k == amount:
                amount = k
                break
    answer = resolution_1*resolution_2*(amount+opacity)/(8*1024**(measure-1))
    if answer == int(answer):
        print('Ваш ответ:', int(answer), meas[measure])
    else:
        print('Ваш ответ:', answer, meas[measure])