file = open(r'Путь к файлу')
min_sum = 20001
count = 0
file_list = []
for i in file:
    i = i.strip('\n')
    file_list.append(int(i))
for i in range(len(file_list)-1):
    if 'Условие':
        count += 1
        if file_list[i] + file_list[i+1] < min_sum:
            min_sum = file_list[i] + file_list[i+1]   #Минимальная сумма
print(count)
print(min_sum)
