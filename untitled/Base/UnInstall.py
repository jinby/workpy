# coding:utf-8
import win32api
import win32con
import sys
import os
import shutil

'''
def getmsiinfo(name):
    i = 0
    msi_info = {}
    user = []
    key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData')
    try:
        for item in win32api.RegEnumKey(key)
            subkey = .EnumKey(key, i)
            user.append(subkey)
            i += 1
    except:
        pass
    for msikey in user:
        j = 0
        filekey = msikey
        msikey = msikey + r"""\Products"""
        deltmp = msikey
        msikey = _winreg.OpenKey(key, msikey)
        try:
            while 1:
                # 得到name和product
                infokey = _winreg.EnumKey(msikey, j)
                msi_info['product'] = infokey
                infokey = infokey + r"""\InstallProperties"""
                infokey = _winreg.OpenKey(msikey, infokey)
                (msiname, type) = _winreg.QueryValueEx(infokey, "DisplayName")
                msi_info['name'] = msiname
                # 得到卸载项
                (unin, type) = _winreg.QueryValueEx(infokey, "UninstallString")
                unin = unin[14:]
                msi_info['unin'] = unin
                if msi_info['name'] == name:
                    deletelist.append(
                        'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\\' + deltmp + '\\' +
                        msi_info['product'])
                    deletelist.append('HKEY_CURRENT_USER\Software\Microsoft\Installer\Products\\' + msi_info['product'])
                    deletelist.append('HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Installer\Products\\' + msi_info['product'])
                    deletelist.append('HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Installer\Features\\' + msi_info['product'])
                    deletelist.append(
                        'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\\' + msi_info['unin'])
                    (file, type) = _winreg.QueryValueEx(infokey, "LocalPackage")
                    deletelist.append(file)
                    filekey = filekey + '\\' + 'Components' + '\\' + msi_info['product']
                    filekey = _winreg.OpenKey(key, filekey)
                    (file, type) = _winreg.QueryValueEx(filekey, msi_info['product'])
                    deletelist.append(file)
                    deletelist.append('C:\\Windows\\Installer\\' + msi_info['unin'])
                    return msi_info
                else:
                    j += 1
        except:
            pass


def delmsi(list):
    for item in list:
        print
        item
        try:
            if item.find('.') != -1:
                os.remove(item)
            elif item.find(':') != -1:
                shutil.rmtree(item, True)
            elif item.find('HKEY') != -1:
                print
                item
                tmpl = item.split('\\', 2)
                key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, tmpl[1])
                _winreg.DeleteKey(key, tmpl[2])
        except:
            pass


if __name__ == "__main__":
    name = sys.argv[1]
    deletelist = []
    getmsiinfo(name)
    delmsi(deletelist)


'''