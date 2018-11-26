import os
import win32api
import win32con
from Base.WindowsUtil import *
import sys

class CdgRegHelp():
    @staticmethod
    def WriteCdgKey():


        key = win32api.RegOpenKey(win32con.HKEY_CLASSES_ROOT, '\\*\\shell\\'  )
        subkey = win32api.RegCreateKey(key, "CDG_Put_In")
        win32api.RegSetValue(subkey,'',win32con.REG_SZ,'CDG_Put_In')
        subkey2 = win32api.RegCreateKey(subkey, r'command')
        win32api.RegSetValue(subkey2, '', win32con.REG_SZ, '\"%s\" \"%s\" -f \"%%1\"' % ( WindowsUtil.FindPythonExe(),os.path.join(os.getcwd(),"Base/CmdHelp.py")) )
        win32api.CloseHandle(subkey2)
        win32api.CloseHandle(subkey)

        key = win32api.RegOpenKey(win32con.HKEY_CLASSES_ROOT, '\\Directory\\Background\\shell\\'  )

        subkey = win32api.RegCreateKey(key, "CDG_Clear_Out")
        win32api.RegSetValue(subkey,'',win32con.REG_SZ,'CDG_Clear_Out')
        subkey2 = win32api.RegCreateKey(subkey, r'command')
        win32api.RegSetValue(subkey2, '', win32con.REG_SZ, '\"%s\" \"%s\" -c'% ( WindowsUtil.FindPythonExe(),os.path.join(os.getcwd(),"Base/CmdHelp.py")))
        win32api.CloseHandle(subkey2)
        win32api.CloseHandle(subkey)

        subkey = win32api.RegCreateKey(key, "CDG_Copy_To")
        win32api.RegSetValue(subkey,'',win32con.REG_SZ,'CDG_Copy_To')
        subkey2 = win32api.RegCreateKey(subkey, r'command')
        win32api.RegSetValue(subkey2, '', win32con.REG_SZ, '\"%s\" \"%s\" -t \"%%V\"' % ( WindowsUtil.FindPythonExe(),os.path.join(os.getcwd(),"Base/CmdHelp.py")) )
        win32api.CloseHandle(subkey2)
        win32api.CloseHandle(subkey)
        win32api.CloseHandle(key)



if __name__ == '__main__':
    print(os.path.join(os.getcwd(),r"Base/CmdHelp.py"))
