import os
print("Select action \n- Encrypt with table \n- Encrypt with hash algorithm \n")
while True:
    action = input().lower()
    if action == "encrypt with table":
        os.system("table_coding.py")
        break
    elif action == "encrypt with hash algorithm":
        os.system("md5.py")
        break
    else:
        print("Please, select something from the proposed")