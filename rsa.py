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
    print("Encrypt or decrypt?")
    while True:
        selection = input().lower()
        if selection == "encrypt":
            print("You alredy have rsa key?")
            key_selection = input().lower()
            if key_selection == "no":
                # Генерация необходимых переменных для RSA
                p = rsa_service.rsa_keygen_p()
                q = rsa_service.rsa_keygen_q()
                n = rsa_service.rsa_keygen_n(p,q)
                eiler = rsa_service.rsa_keygen_eiler(p,q)
                e = rsa_service.rsa_keygen_e(eiler)
                d = rsa_service.rsa_keygen_d(eiler,e)
                # Запись открытого ключа
                print("Enter directory to save rsa public key:")
                openkey_path = input()
                openkey_save = open(openkey_path,'w')
                openkey_save.write(str(e))
                openkey_save.write(" ")
                openkey_save.write(str(n))
                openkey_save.close()
                # Запись секретного ключа
                print("Enter directory to save rsa private key:")
                privatekey_path = input()
                privatekey_save = open(privatekey_path, 'w')
                privatekey_save.write(str(d))
                privatekey_save.write(" ")
                privatekey_save.write(str(n))
            else:
                print("Enter path to the public rsa key")
                key_in_path = input()
                try:
                    key_in = open(key_in_path, 'r').read()
                except FileNotFoundError:  # Если файл не найден
                    print("Error: file not found")
                    break
                except IsADirectoryError:  # Введён некорректный путь
                    print("Error: entered path to the directory, not to file")
                    break
                except PermissionError:  # Недостаточно прав для доступа к файлу\директории
                    print("Error: you don't have permission to this file\directory")
                    break
                e = int(key_in[:key_in.find(" ")])
                n = int(key_in[key_in.find(" ")+1:])
            # Шифрование сообщения
            fout = ""
            for i in range(len(file)):
                fout += str((ord(file[i])**e)%n) + " "
            # Запись зашифрованного сообщения
            fout_save = open(fpath,'w')
            fout_save.write(fout)
            break
        elif selection == "decrypt":
            # Ввод секретного ключа
            print("Enter path to the private key")
            privatekey_path = input()
            # Обработка ошибок файлового ввода
            try:
                privatekey = open(privatekey_path, 'r').read()
            except FileNotFoundError:  # Если файл не найден
                print("Error: file not found")
                break
            except IsADirectoryError:  # Введён некорректный путь
                print("Error: entered path to the directory, not to file")
                break
            except PermissionError:  # Недостаточно прав для доступа к файлу\директории
                print("Error: you don't have permission to this file\directory")
                break
            # Считывание секретного ключа
            d = int(privatekey[:privatekey.find(" ")])
            n = int(privatekey[privatekey.find(" ")+1:])
            # Разшифровка
            fout = ""
            for i in range(file.count(" ")):
                tmp = int(file[:file.find(" ")])
                file = file[file.find(" ")+1:]
                res = (tmp**d) % n
                fout += str(chr(res))
                print(file)
            # Запись полученного сообщения
            fout_save = open(fpath, 'w')
            fout_save.write(fout)
            break
        else:
            print("Please, select something from the proposed")
    break