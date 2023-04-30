import os
while True:
    os.system("clear")
    print("[1]Custom sms Seever 1\n[2]Custom sms Server 2\n")
    opt=str(input("[®] Enter Your Option:- "))
    if opt=="1":
         os.system("python3 cmdsms.py")
    elif opt=="2":
        os.system(" python3 cmdotpsms.py")