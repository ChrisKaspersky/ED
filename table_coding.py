while True:  # Для возможности при ошибке остановить программу с помощью break
    # Ввод пути таблицы
    print("Table path:")
    tpath = input()
    # Проверка корректности ввода пути таблицы
    try :
        table = open(tpath).read()
    except FileNotFoundError:  # Если файл не найден
        print("Error: table not found")
        break
    except IsADirectoryError:  # Введён некорректный путь
        print("Error: entered path to the directory, not to file")
        break
    except PermissionError:  # Недостаточно прав для доступа к файлу\директории
        print("Error: you don't have permission to this file\directory")
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
        print("Error: file not found")  # Если файл не найден
        break
    except IsADirectoryError:  # Введён некорректный путь
        print("Error: entered path to the directory, not to file")
        break
    except PermissionError:  # Недостаточно прав для доступа к файлу\директории
        print("Error: you don't have permission to this file\directory")
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
        print("Error: unknown method")
        break
    # Файловый вывод
    fileout = open(fpath,'w')
    fileout.write(file)
    fileout.close()
    break