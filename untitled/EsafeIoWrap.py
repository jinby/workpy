# coding:utf-8
import win32gui
import time
import win32con
import os
import shutil
from Base.WindowsUtil import *

# 消息对应 https://blog.csdn.net/lostspeed/article/details/60778784

classname = r""
titlename = r"ESAFENET -- http://www.esafenet.com"

class NetSafeIoHelp:
    def __init__(self):
        pass

    def openIo(self):
        pass

    def inputPassword(self):
        #先试探主窗口句柄
        hwndFileLock = win32gui.FindWindow( None, "FileLock Test - ESAFENET(http://www.esafenet.com)")
        if (hwndFileLock == 0) :
            #获取登录窗口
            hwndLogin = win32gui.FindWindowEx(None, None, None, "ESAFENET -- http://www.esafenet.com")
            print('find Login Window handle = %X' % hwndLogin)
            if ( hwndLogin ):
                left, top, right, bottom = win32gui.GetWindowRect(hwndLogin)
                print(left, top, right, bottom)
                time.sleep(0.4)
                hEdit = win32gui.GetDlgItem(hwndLogin, 0x410)
                #print('find hEdit Window handle = %d' % hEdit)
                win32gui.SendMessage(hEdit, win32con.WM_SETTEXT, 0, "EsafeNetIo")
                time.sleep(0.2)
                hBtnOK = win32gui.GetDlgItem(hwndLogin, 0x1)
                print('find hBtnOK Window handle = %X' % hBtnOK)
                win32gui.SendMessage(hBtnOK, win32con.WM_LBUTTONDOWN)
                win32gui.SendMessage(hBtnOK, win32con.WM_LBUTTONUP)
                time.sleep(0.3)

    def relate(self):
        #获取窗口左上角和右下角坐标
        hwndFileLock = win32gui.FindWindow( None, "FileLock Test - ESAFENET(http://www.esafenet.com)")
        if (hwndFileLock) :
            print('find hwndFileLock Window handle = %X' % hwndFileLock)

            hBtnStartRelate = win32gui.GetDlgItem(hwndFileLock, 0x41C)
            win32gui.SendMessage(hBtnStartRelate, win32con.WM_LBUTTONDOWN)
            win32gui.PostMessage(hBtnStartRelate, win32con.WM_LBUTTONUP)
            #time.sleep(0.1)
            #win32api.keybd_event(13, 0 )
            #win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)

            time.sleep(0.5)
            hwndDlgOk = win32gui.FindWindow(None, "Iotest64")
            if ( hwndDlgOk == 0 ) :
                hwndDlgOk = win32gui.FindWindow(None, "Iotest")

            if (hwndDlgOk) :
                hBtnDlgOkBtnOK = win32gui.GetDlgItem(hwndDlgOk, 0x2)
                win32gui.SendMessage(hBtnDlgOkBtnOK, win32con.WM_LBUTTONDOWN )
                win32gui.SendMessage(hBtnDlgOkBtnOK, win32con.WM_LBUTTONUP )

            time.sleep(0.2)

            hBtnFilterStop = win32gui.GetDlgItem(hwndFileLock, 0x3E8)
            win32gui.SendMessage(hBtnFilterStop, win32con.WM_LBUTTONDOWN )
            win32gui.SendMessage(hBtnFilterStop, win32con.WM_LBUTTONUP)

            time.sleep(0.2)

            hBtnLogStop = win32gui.GetDlgItem(hwndFileLock, 0x3EB)
            win32gui.SendMessage(hBtnLogStop, win32con.WM_LBUTTONDOWN)
            win32gui.SendMessage(hBtnLogStop, win32con.WM_LBUTTONUP)

    def moverecvfile(self):
        cdg_path = ''
        if WindowsUtil.is64Windows():
            cdg_path = os.path.join( WindowsUtil.getProgramFiles64(), r'EsafeNet\Cobra DocGuard Client')
        else:
            cdg_path = os.path.join(WindowsUtil.getProgramFiles32(), r'EsafeNet\Cobra DocGuard Client')

        path = os.path.join(os.getcwd() , "recv")
        for dir_path, dir_name, file_names in  cdg_path.walk( path ):
            for file_path in file_names:
                dstfile = os.path.join(cdg_path , file_path)
                if (os.path.exists(dstfile)):
                    for i in range(100):
                        bkfile = "%s%s%d" % (dstfile ,'.bk',  i )
                        if ( os.path.exists( bkfile) == False ):
                            os.rename( dstfile, bkfile )
                            break
                    srcfile = os.path.join(dir_path, file_path)
                    shutil.move( srcfile, dstfile)
                    print("copy %s -> %s" % (srcfile, dstfile))

if __name__ == "__main__":
    ih = NetSafeIoHelp()
    ih.inputPassword()
    ih.relate()
