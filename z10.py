inp = input('Введите выражение: ')
digits = int(input('Введите количество разрядов: '))
answer = int(bin(eval(inp))[2:], 2)
print(answer)