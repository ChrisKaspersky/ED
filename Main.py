# Ввод таблицы
print("Table path:")
tpath = input()
table = open(tpath).read()
# Массивы под таблицу
Decoded = []
Encoded = []
# Заполнение массивов
for i in range(table.count('\n')):
    Decoded.append(table[:table.find('=')-1])
    table = table[table.find('=')+2:]
    Encoded.append(table[:table.find('\n')])
    table = table[table.find('\n')+1:]
# Ввод файла
print("File path:")
fpath = input()
file = open(fpath).read()
# Выбор нужного действия
print("Encode/Decode:")
methd = input()
# Выполнение метода
if methd == "Decode":
    for i in range(1,len(Encoded)+1):
        file = file.replace(Encoded[-i],Decoded[-i])
elif methd == "Encode":
    for i in range(1,len(Encoded)+1):
        file = file.replace(Decoded[-i],Encoded[-i])
else:
    print("Unknown method")
# Файловый вывод
fileout = open(fpath,'w')
fileout.write(file)
fileout.close()
