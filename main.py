a = int(input('введите количество строк ')) #запрашиваем колво строк
while a <=0: #цикл
    a = int(input('введите количество строк ')) #если число отрицательное
lines = [] #
for i in range(a):
    line = input('введите строку ')
    lines.append(line)
text = ' '.join(lines)
words = text.split()
w = set(words)
print(f'количество слов {len(w)}')