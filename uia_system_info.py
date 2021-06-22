import subprocess
import sys
import os

REPO_ROOT = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, REPO_ROOT)

LIB_PATH = os.path.join(REPO_ROOT, "lib")
sys.path.append(LIB_PATH)

from system_info import *
from lib import uiautomation as auto
auto.uiautomation.SetGlobalSearchTimeout(15)  # set new timeout 15

xtu_exe = r"C:\Program Files\Intel\Intel(R) Extreme Tuning Utility\Client\XtuUiLauncher.exe"


def uia_get_system_info_list():
    """Extract information from XUT GUI window. Then return the system information in dict and 
       output the dict in a json file.
    Args:
        None

    Returns:
        dict_ (dict): System information extract from XUT System Pane.
    """
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

    system_info_dict = get_all_system_info(text)
    # wb will preserve the unicode UTF-8 format so that can write "®" to file.
    with open("system_info.json", "wb") as f:
        f.write(json.dumps(system_info_dict, sort_keys=False, ensure_ascii=False, indent=4).encode('utf8'))


    subprocess.call("taskkill /f /im XtuUiLauncher.exe")
    subprocess.call("taskkill /f /im XtuService.exe")
    subprocess.call("taskkill /f /im PerfTune.exe")

uia_get_system_info_list()