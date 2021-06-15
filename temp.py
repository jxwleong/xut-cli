import subprocess
import sys
import time
import uiautomation as auto
auto.uiautomation.SetGlobalSearchTimeout(15)  # set new timeout 15

xtu_exe = r"C:\Program Files\Intel\Intel(R) Extreme Tuning Utility\Client\XtuUiLauncher.exe"
prime95=r"G:\MyProjects\xprime95\p95v303b6.win32\prime95.exe"

SysInfo = {
    # PROCESSOR
    "brand_string": "SystemInfo:ProcessorBrandString",
    "family_string": "SystemInfo:ProcessorFamilyString",
    "physical_core": "SystemInfo:ProcessorPhysicalCpuCores",
    "logical_core": "SystemInfo:ProcessorLogicalCpuCores" ,
    "possible_turbo_bins": "SystemInfo:ProcessorOverclockableTurboBins",
    "turbo_overclockable": "SystemInfo:ProcessorTurboOverclockable",
    "feature_flags": "SystemInfo:ProcessorFeatureFlags",
    "instructions": "SystemInfo:ProcessorInstructions",
    "intel_turbo_boost_max": "SystemInfo:ProcessorFavoredCoreSupported",
    "intel_speed_shift": "SystemInfo:ProcessorHwpEnabled",
    "microcode_update": "SystemInfo:ProcessorMicrocodeUpdate",
    "hybrid_core": "SystemInfo:ProcessorIsHybridArchitecture",            

    # Graphics
    "graphic_0": "SystemInfo:GraphicsName0",
    "gfx0_compatibility": "SystemInfo:GraphicsCompatibility0",
    "gfx0_ram": "SystemInfo:GraphicsRAM0",
    "gfx0_dac": "SystemInfo:GraphicsDACType0",
    "gfx0_driver_version": "SystemInfo:GraphicsDriverVersion0",
    "gfx0_driver_date": "SystemInfo:GraphicsDriverDate0",

    "graphic_1": "SystemInfo:GraphicsName1",
    "gfx1_compatibility": "SystemInfo:GraphicsCompatibility1",
    "gfx1_ram": "SystemInfo:GraphicsRAM1", 
    "gfx1_dac": "SystemInfo:GraphicsDACType1",
    "gfx1_driver_version": "SystemInfo:GraphicsDriverVersion1",
    "gfx1_driver_date": "SystemInfo:GraphicsDriverDate1",

    # Operating System
    "os_manufacturer": "SystemInfo:OperatingSystemManufacturer",
    "os_name": "SystemInfo:OperatingSystemName",
    "os_version": "SystemInfo:OperatingSystemVersion",
    "os_service_pack": "SystemInfo:OperatingSystemServicePack",
    "os_system_name": "SystemInfo:OperatingSystemSystemName",
    "os_boot_device": "SystemInfo:OperatingSystemBootDevice",

    # Watchdog
    "watchdog_support": "SystemInfo:WatchdogWatchdogPresent",
    "watchdog_run_at_boot": "SystemInfo:WatchdogRunningAtBoot",
    "watchdog_failed": "SystemInfo:WatchdogFailed",

    # Memory
    #"memory_installed": "SystemInfo:MemoryTotalInstalledMemory",
    #"memory_bank0": "SystemInfo:MemoryBankLabel0",
    #"memory_
}

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

    for key, value in SysInfo.items():
        text = window.TextControl(searchDepth=3, ClassName="TextBlock", AutomationId=value)
        print(f"{key}: {text.Name}")

    text = window.TextControl(searchDepth=3, ClassName="TextBlock", AutomationId="SystemInfo:ProcessorBrandString")
    print(text)
    print(type(text))
    print(text.Name)

    text = window.TextControl(searchDepth=3, ClassName="TextBlock", AutomationId="SystemInfo:ProcessorFamilyString")
    print(text)
    print(type(text))
    print(text.Name)    
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
    main()
    sys.exit(0)
