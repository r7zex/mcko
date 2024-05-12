from itertools import *


outputs = list(map(int, list(input('Введите выходные данные, НЕ разделяя их пробелами (столбец F): '))))
actions = list(product(['and', 'or'], repeat=2))
inverse = list(product(['not', ''], repeat=3))
index = 0
ans = ''
for i in inverse:
    for k in actions:
        Test = True
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    formula = f'{i[0]} {str(a)} {k[0]} {i[1]} {str(b)} {k[1]} {i[2]} {str(c)}'

                    out = int(eval(formula))
                    if out != outputs[index]:
                        index = 0
                        Test = False
                    else:
                        index += 1
        if Test:
            ans = f'{i[0]} A {k[0]} {i[1]} B {k[1]} {i[2]} C'
        index = 0
print(ans)