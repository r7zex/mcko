methods = input('Введите все возможные команды, раздеяя их пробеами: ').split()
start = int(input('Введите начальное число: '))
need = list(map(int, input('Введите через пробел числа, через которые код должен пройти (0 при отсутствии): ').split()))
stop = list(map(int, input('Введите через пробел числа, через которые код НЕ должен пройти (0 при отсутствии): ').split()))
end = int(input('Введите конечное число: '))
count = 0
def f(x, y):
    if x > y or x in stop:
        return 0
    if x == y:
        return 1
    else:
        func = "f(eval(f'x {methods[0]}'), y)"
        for i in range(1, len(methods)):
            func += "+ f(eval(f'x {methods["+f"{i}" + "]}'), y)"
        return eval(func)
if need[0] != 0:
    answer = 'f(start, need[0])'
    for k in range(1, len(need)):
        answer += '* f(need[k-1], need[k])'
    answer += '* f(need[-1], end)'
    print(eval(answer))
else:
    print(f(start, end))