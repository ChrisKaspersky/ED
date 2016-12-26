while True:
    # Ввод таблицы
    print("Table path:")
    tpath = input()
    try :
        table = open(tpath).read()
    except FileNotFoundError:
        print("Ошибка: таблица не найдена")
        break
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
    try :
        file = open(fpath).read()
    except FileNotFoundError:
        print("Ошибка: файл не найден")
        break
    # Выбор нужного действия
    print("Encrypt/Decrypt:")
    methd = input()
    # Выполнение метода
    if methd == "Decrypt":
        for i in range(1,len(Encoded)+1):
            file = file.replace(Encoded[-i],Decoded[-i])
    elif methd == "Encrypt":
        for i in range(1,len(Encoded)+1):
            file = file.replace(Decoded[-i],Encoded[-i])
    else:
        print("Ошибка: неизвестное действие")
        break
    # Файловый вывод
    fileout = open(fpath,'w')
    fileout.write(file)
    fileout.close()
