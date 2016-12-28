import os
print("Choose encrypting algorithm \n- table \n- md5 \n- sha-1\n- rsa")
while True:
    action = input().lower()
    if action == "table":
        os.system("table_coding.py")
        break
    elif action == "md5":
        os.system("md5.py")
        break
    elif action == "sha-1":
        os.system("sha1.py")
        break
    elif action == "rsa":
        os.system("rsa.py")
        break
    else:
        print("Please, select something from the proposed")