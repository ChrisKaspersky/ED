import os
print("Select action \n- Encrypt with table \n- Encrypt with md5 hash algorithm \n- Encrypt with SHA hash algorithm")
while True:
    action = input().lower()
    if action == "encrypt with table":
        os.system("table_coding.py")
        break
    elif action == "encrypt with md5 hash algorithm":
        os.system("md5.py")
        break
    elif action == "encrypt with SHA hash algorithm":
        os.system("sha1.py")
        break
    else:
        print("Please, select something from the proposed")