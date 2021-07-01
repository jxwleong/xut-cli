from enum import Enum
import subprocess
import sys
import os
import time
import xml.etree.ElementTree as ET
from xml.dom import minidom

REPO_ROOT = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, REPO_ROOT)

LIB_PATH = os.path.join(REPO_ROOT, "lib")
sys.path.append(LIB_PATH)

from system_info import *
from lib import uiautomation as auto
from lib.dicttoxml import dicttoxml

auto.uiautomation.SetGlobalSearchTimeout(15)  # set new timeout 15

xtu_exe = r"C:\Program Files\Intel\Intel(R) Extreme Tuning Utility\Client\XtuUiLauncher.exe"

def get_supported_stress_test():
    proc = subprocess.Popen(xtu_exe)
    window = auto.WindowControl(searchDepth=1, ClassName="Window", Name="Intel® Extreme Tuning Utility")

    if auto.WaitForExist(window, 30):
        print("Window found!")
    else:
        print("Window don't exists!")

    stress_test_custom = auto.CustomControl(searchDepth=4, ClassName="StressTestView")
    checkbox = []
    for item, depth in auto.WalkControl(stress_test_custom, includeTop=True):
        if item.ClassName == "CheckBox":
            print(type(item))
            ToggleButton = item.GetTogglePattern()
            print(f"BEFORE toggle {item.Name}")
            print(ToggleButton.ToggleState)
            item.GetTogglePattern().Toggle()
            print(f"AFTER toggle {item.Name}")
            print(ToggleButton.ToggleState)
            checkbox.append(item.Name)
    print(checkbox)

    time.sleep(3)
    subprocess.call("taskkill /f /im XtuUiLauncher.exe")
    subprocess.call("taskkill /f /im XtuService.exe")
    subprocess.call("taskkill /f /im PerfTune.exe")
    return checkbox
    
get_supported_stress_test()