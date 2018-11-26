import win32clipboard
import win32api
import win32con
import sys
import os

class WindowsUtil:

    @staticmethod
    def is64Windows():
        return 'PROGRAMFILES(X86)' in os.environ

    @staticmethod
    def getProgramFiles32():
        if WindowsUtil.is64Windows():
            return os.environ['PROGRAMFILES(X86)']
        else:
            return os.environ['PROGRAMFILES']

    @staticmethod
    def getProgramFiles64():
        if WindowsUtil.is64Windows():
            return os.environ['PROGRAMW6432']
        else:
            return None

    @staticmethod
    def getcliptext():
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData(win32con.CF_TEXT)
        win32clipboard.CloseClipboard()
        return str(text,encoding="utf8")

    @staticmethod
    def setcliptext(text):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_TEXT, bytes(text, encoding = "utf8"))
        win32clipboard.CloseClipboard()

    @staticmethod
    def killProcessByName(process_name):
        os.system('taskkill /IM %s /F' % process_name)
        print('kill %s' % process_name)

    @staticmethod
    def openProcessByNameOs(process_path):
        if (os.path.exists(process_path)):
            os.system(process_path)
            print('run %s' % process_path)

    @staticmethod
    def openProcessByNameWin32(process_path):
        win32api.ShellExecute(None, "open", process_path, None, None, win32con.SW_SHOWNORMAL)

    @staticmethod
    def FindPythonExe():
        for spath in sys.path:
            exepath = os.path.join(spath, "python.exe")
            if os.path.exists(exepath):
                return exepath
        return None

if __name__ == '__main__':
    print(WindowsUtil.getProgramFiles32())
    print(WindowsUtil.getProgramFiles64())

    WindowsUtil.setcliptext(r"测试")
    print(WindowsUtil.getcliptext())

