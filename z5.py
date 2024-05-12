def per(number, base):
    global letters
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
    number = str(number)
    number_1 = []
    number_2 = []
    parts[0] = int(parts[0])
    parts[1] = float('0.'+parts[1])
    while parts[0] > 0:
        number_1.insert(0, parts[0] % base)
        parts[0] = parts[0] // base
    check = 0
    mult = 1
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



letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''
number = input('Введите число: ')
shift = int(input('Введите величину сдвига: '))
number = per(number, 2)
if list(number)[0] == '-':
    answer += '1'
    number = number.replace('-', '')
else:
    answer += '0'
index = number.index(',')
shift += index - 1
answer += '0'*(8-len(bin(shift)[2:]))+str(bin(shift)[2:])
number = number.replace(',', '')
number = list(number)
number.insert(1, ',')
number = ''. join(number).split(',')[1]
answer += number
answer += '0' * (32-len(answer))
start = 0
ans_1 = []
ans_2 = []
for i in range(4, 33, 4):
    ans_1.append(list(answer)[start:i])
    start += 4
for i in ans_1:
    i = ''.join(i)
    i = int(i, 2)
    if i > 9:
        ans_2.append(letters[i-10])
    else:
        ans_2.append(i)
print(''.join(list(map(str, ans_2))))