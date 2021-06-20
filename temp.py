import subprocess
import os
import sys
import time

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, ROOT_DIR)

LIB_PATH = os.path.join(ROOT_DIR, "lib")
sys.path.append(LIB_PATH)

from lib import uiautomation as auto
auto.uiautomation.SetGlobalSearchTimeout(15)  # set new timeout 15

xtu_exe = r"C:\Program Files\Intel\Intel(R) Extreme Tuning Utility\Client\XtuUiLauncher.exe"
prime95=r"G:\MyProjects\xprime95\p95v303b6.win32\prime95.exe"

excluded_sysinfo_text = ["Welcome to Intel Extreme Tuning Utility",
            ("Intel Extreme Tuning Utility is a state-of-the-art overclocking solution for Intel IA-based platforms. " +
            "It is a comprehensive set of tools to tune, test and monitor your system. " +
            "Click on the link to learn more about  Overclocking  and  XTU"),
            "How do I overclock with it?", 
            "The platform does not support overclocking. For best Overclocking performance, please check Intel K- and X-series Processors."]
sysinfo_title = ["Processor", "Graphics", "Operating System", "Watchdog", "Memory", "BIOS", "Motherboard", "XTU"]

def sys_info():
    text = []
    proc = subprocess.Popen(xtu_exe)
    window = auto.WindowControl(searchDepth=1, ClassName="Window", Name="Intel® Extreme Tuning Utility")

    if auto.WaitForExist(window, 30):
        print("Window found!")
    else:
        print("Window don't exists!")

    system_info_custom = auto.CustomControl(searchDepth=2, ClassName="SystemInfoView")
    for item, depth in auto.WalkControl(system_info_custom, includeTop=True):
        if item.Name not in  excluded_sysinfo_text and  \
        item.ClassName == "TextBlock":
               text.append(item.Name)

    print(text)
    # Reference: https://stackoverflow.com/a/21752685
    it = iter(text)
    for x in it:
        if x in sysinfo_title:
            print("\n")
            print(x)    
        else:
            if x in ["Bank Label"]:
                print("")
            print(f"{x}: {next(it)}")

    subprocess.call("taskkill /f /im XtuUiLauncher.exe")
    subprocess.call("taskkill /f /im XtuService.exe")
    subprocess.call("taskkill /f /im PerfTune.exe")

def get_supported_stress_test():
    proc = subprocess.Popen(xtu_exe)
    window = auto.WindowControl(searchDepth=1, ClassName="Window", Name="Intel® Extreme Tuning Utility")

    if auto.WaitForExist(window, 30):
        print("Window found!")
    else:
        print("Window don't exists!")

    stress_test_custom = auto.CustomControl(searchDepth=2, ClassName="StressTestView")
    print("Supported Stress Test")
    for item, depth in auto.WalkControl(stress_test_custom, includeTop=True):
        if item.ClassName == "CheckBox":
            print(item.Name)

    subprocess.call("taskkill /f /im XtuUiLauncher.exe")
    subprocess.call("taskkill /f /im XtuService.exe")
    subprocess.call("taskkill /f /im PerfTune.exe")

def main():
    proc = subprocess.Popen(xtu_exe)
    window = auto.WindowControl(searchDepth=1, ClassName="Window", Name="Intel® Extreme Tuning Utility")
    print("BEFORE")
    #window = auto.WindowControl(searchDept=1, Name="Prime95")
    print("AFTER")
    if auto.WaitForExist(window, 30):
        print('FOUND!')
    else:
        print('NOT!')
    #exit(0)
    print(window)
    print("HELL")

    # edit = window.ButtonControl(searchDepth=2, ClassName="Button", AutomationId="Navigation:StressTesting")
    # print(type(edit))
    # edit.Click()
    
    # checkbox = window.CheckBoxControl(searchDepth=3, ClassName="CheckBox", AutomationId="StressTestSelected:CpuTest")
    # print(type(checkbox))
    # print(checkbox)
    # checkbox.GetTogglePattern().Toggle()

    # start = window.ButtonControl(searchDepth=3, ClassName="Button", AutomationId="StressTestStartButton")
    # print(type(start))
    # start.Click()
    
    # time.sleep(5)

    # end = window.ButtonControl(searchDepth=3, ClassName="Button", AutomationId="StressTestStopButton")
    # print(type(end))
    # end.Click()

    #proc.terminate()
    # subprocess.call("taskkill /f /im XtuUiLauncher.exe")
    # subprocess.call("taskkill /f /im XtuService.exe")
    # subprocess.call("taskkill /f /im PerfTune.exe")
    #edit.GetValuePattern().SetValue('Hello')
    # when calling SendKeys, uiautomation starts to search window and edit in 15 seconds
    # because SendKeys indirectly calls Control.Element and Control.Element is None
    # if window and edit don't exist in 15 seconds, a LookupError exception will be raised
    # try:
    #     edit.SendKeys('first notepad')
    # except LookupError as ex:
    #     print("The first notepad doesn't exist in 15 seconds")
    #     return
    # # the second call to SendKeys doesn't trigger a search, the previous call makes sure that Control.Element is valid
    # edit.SendKeys('{Ctrl}a{Del}')
    # window.GetWindowPattern().Close()  # close the first Notepad, window and edit become invalid even though their Elements have a value

    # subprocess.Popen('notepad.exe')  # run second Notepad
    # window.Refind()  # need to refind window, trigger a new search
    # edit.Refind()  # need to refind edit, trigger a new search
    # edit.SendKeys('second notepad')
    # edit.SendKeys('{Ctrl}a{Del}')
    # window.GetWindowPattern().Close()  # close the second Notepad, window and edit become invalid again

    # subprocess.Popen('notepad.exe')  # run third Notepad
    # if window.Exists(3, 1): # trigger a new search
    #     if edit.Exists(3):  # trigger a new search
    #         edit.SendKeys('third notepad')  # edit.Exists makes sure that edit.Element has a valid value now
    #         edit.SendKeys('{Ctrl}a{Del}')
    #     window.GetWindowPattern().Close()
    # else:
    #     print("The third notepad doesn't exist in 3 seconds")


if __name__ == '__main__':
    #main()
    sys_info()
    #get_supported_stress_test()
    sys.exit(0)
