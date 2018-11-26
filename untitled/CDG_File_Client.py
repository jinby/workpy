from Base.Socket_Client import *
from netsafeiohelp import NetSafeIoHelp

if __name__ == '__main__' :

    while True:
        a = input("请输入正确的值（0-3）：")
        if a== "0":
            print('End')
            break;
        elif a == "1":
            recvallfile()
        elif a == "2":
            ni = NetSafeIoHelp()
            ni.moverecvfile()
        elif a == "3":
            pass

