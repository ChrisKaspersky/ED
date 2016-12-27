while True:  # Для возможности при ошибке остановить программу с помощью break
    # Ввод пути таблицы
    print("Table path:")
    tpath = input()
    # Проверка корректности ввода пути таблицы
    try :
        table = open(tpath).read()
    except FileNotFoundError:  # Если файл не найден
        print("Ошибка: таблица не найдена")
        break
    except IsADirectoryError:  # Введён некорректный путь
        print("Ошибка: введён путь к директории, а не файлу")
        break
    except PermissionError:  # Недостаточно прав для доступа к файлу\директории
        print("Ошибка: недостаточно прав для доступа")
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
    # Ввод пути файла
    print("File path:")
    fpath = input()
    # Проверка корректности ввода пути к файлу
    try :
        file = open(fpath).read()
    except FileNotFoundError:
        print("Ошибка: файл не найден")  # Если файл не найден
        break
    except IsADirectoryError:  # Введён некорректный путь
        print("Ошибка: введён путь к директории, а не файлу")
        break
    except PermissionError:  # Недостаточно прав для доступа к файлу\директории
        print("Ошибка: недостаточно прав для доступа")
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
    break