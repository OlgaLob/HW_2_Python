# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в 
# файле file.txt в одной строке одно число.
num = int(input('Введите целое число: '))
lst = list()
if (num > 0):
    for i in range(- num, num + 1):
     lst.append(i)
else:
    for i in range(- num, num - 1, -1):
        lst.append(i)
print(lst)
res = 1
path = 'file.txt'
data = open(path, 'r')
for i in data:
    res = res * lst[int(i)]
data.close()
print(f'Произведение элементов списка на позициях, указанных в файле file.txt, равно {res}')

