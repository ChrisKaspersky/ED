import rsa_service
while True:
    # Файловый ввод
    print("File path:")
    fpath = input()
    try:
        file = open(fpath, 'r').read()
    except FileNotFoundError:  # Если файл не найден
        print("Error: file not found")
        break
    except IsADirectoryError:  # Введён некорректный путь
        print("Error: entered path to the directory, not to file")
        break
    except PermissionError:  # Недостаточно прав для доступа к файлу\директории
        print("Error: you don't have permission to this file\directory")
        break
    # Генерация необходимых переменных для RSA
    p = rsa_service.rsa_keygen_p()
    q = rsa_service.rsa_keygen_q()
    n = rsa_service.rsa_keygen_n(p,q)
    eiler = rsa_service.rsa_keygen_eiler(p,q)
    e = rsa_service.rsa_keygen_e(eiler)
    d = rsa_service.rsa_keygen_d(eiler,e)
    # Сохранение открытого ключа
    print("Enter directory to save rsa public key:")
    openkey_path = input()
    openkey_save = open(openkey_path,'w')
    openkey_save.write(str(e))
    openkey_save.write(" ")
    openkey_save.write(str(n))
    openkey_save.close()
    # Шифрование сообщения
    fout = ""
    for i in range(len(file)):
        fout += str((ord(file[i])**e)%n) + " "
    # Запись зашифрованного сообщения
    fout_save = open(fpath,'w')
    fout_save.write(fout)
    # Запись секретного ключа
    print("Enter directory to save rsa private key:")
    privatekey_path = input()
    privatekey_save = open(openkey_path,'w')
    privatekey_save.write(str(d))
    privatekey_save.write(" ")
    privatekey_save.write(str(n))
    break