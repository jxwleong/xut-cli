import win32gui

def getShell():
    thelist = []
    def findit(hwnd,ctx):
        if win32gui.GetWindowText(hwnd) == "Intel® Extreme Tuning Utility": # check the title
            thelist.append(hwnd)

    win32gui.EnumWindows(findit,None)
    return thelist

b = getShell()
print(b)
rect = win32gui.GetWindowRect(b)
print(rect)