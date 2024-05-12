def per(number, base):
    number = number.strip(' ')
    if list(number)[0] == '-':
        global minus
        minus = True
        number = number.replace('-', '')
    else:
        minus = False
    if ',' in number:
        parts = number.split(',')
    elif '.' in number:
        parts = number.split('.')
    else:
        parts = [number]
    mult = 0
    first = 0
    second = 0
    for i in parts[0][::-1]:
        first += int(i)*(base**mult)
        mult += 1
    mult = -1
    for i in parts[1]:
        second += int(i)*(base**mult)
        mult -= 1
    return first+second


def per_out(number, base):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = str(number)
    number_1 = []
    number_2 = []
    parts = number.split('.')
    parts[0] = int(parts[0])
    parts[1] = float('0.'+parts[1])
    while parts[0] > 0:
        number_1.insert(0, parts[0] % base)
        parts[0] = parts[0] // base
    check = 0
    mult = 1
    if parts[1] != 0.0:
        while check != 1:
            if parts[1] * (base ** mult) >= 1:
                number_2.append(int(parts[1] * base ** mult))
                mult = 1
                parts[1] = parts[1] * base ** mult - int(parts[1] * base ** mult)
                if parts[1] * base ** mult == int(parts[1] * base ** mult):
                    check = 1
            else:
                mult += 1
                number_2.append(0)
    else:
        number_2 = [0]
    for i in range(len(number_1)):
        if number_1[i] > 9:
            number_1[i] = letters[number_1[i]-10]
    for i in range(len(number_2)):
        if number_2[i] > 9:
            number_2[i] = letters[number_2[i]-10]
    if minus:
        return '-'+''.join(list(map(str, number_1))) + ',' + ''.join(list(map(str, number_2)))
    else:
        return ''.join(list(map(str, number_1))) + ',' + ''.join(list(map(str, number_2)))


print('РЕШАТОР МЦКО ИСКЛЮЧИТЕЛЬНО ДЛЯ ШКОЛЫ 1636')
amount = int(input('Введите количество чисел: '))
numbers = {}
sings = []

for _ in range(amount):
    number = input('Введите число: ')
    base = int(input('Введите основание числа: '))
    numbers[number] = base
for _ in range(amount-1):
    sign = input('Введите знаки соответственно по-одному: ')
    sings.append(sign)
output_base = int(input('Введите конечную систему счисления: '))
place = 0
answer = ''
for i in numbers.items():
    try:
        answer += str(per(i[0], i[1])) + sings[place]
        place += 1
    except:
        answer += str(per(i[0], i[1]))
ans_1 = eval(answer)
ans_out = per_out(ans_1, output_base)
print(ans_out)
