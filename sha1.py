import hashlib
while True:  # Для возможности при ошибке остановить программу с помощью break
    # Файловый ввод
    print("File path:")
    fpath = input()
    try :
        file = open(fpath,'r').read()
    except FileNotFoundError:  # Если файл не найден
        print("Error: file not found")
        break
    except IsADirectoryError:  # Введён некорректный путь
        print("Error: entered path to the directory, not to file")
        break
    except PermissionError:  # Недостаточно прав для доступа к файлу\директории
        print("Error: you don't have permission to this file\directory")
        break
    # Хеширование алгоритмом md5
    hash = hashlib.sha1(file.encode('utf-8')).hexdigest()
    # Запись в файл
    fout = open(fpath)
    fout.write(hash)
    fout.close()
    break
