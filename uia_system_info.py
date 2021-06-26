from enum import Enum
import subprocess
import sys
import os
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


class DataType(Enum):
    Json=1,
    Xml=2,

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
    
    #dict2file("system_info.json", DataType.Json, system_info_dict)
    dict2file("system_info.xml", DataType.Xml, system_info_dict)

    subprocess.call("taskkill /f /im XtuUiLauncher.exe")
    subprocess.call("taskkill /f /im XtuService.exe")
    subprocess.call("taskkill /f /im PerfTune.exe")

def dict2file(file: str, file_type: DataType, data: dict) -> str:
    """Dump data in dict to either json or xml file

    Args:
        file (str): Path to the file 
        file_type (DataType): Type of data (Json or Xml)
        data (dict): Data in dict to be write to file

    Returns:
        return the path of the file (which is same as file argument)
    """
    # wb will preserve the unicode UTF-8 format so that can write "®" to file.
    with open(file, "wb") as f:
        if file_type is DataType.Json:
            f.write(json.dumps(data, sort_keys=False, ensure_ascii=False, indent=4).encode('utf8'))
        else:
            xml_ = dicttoxml(data, attr_type=False)
            tree = ET.ElementTree(ET.fromstring(xml_))
            root = tree.getroot()
            xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
            f.write(xmlstr.encode('utf8'))



    return file


uia_get_system_info_list()