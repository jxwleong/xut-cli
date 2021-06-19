import unittest

import json

list_  = ["Processor", "Brand String", "Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz", "Family", "Skylake", 
        "Physical CPU Cores", "4", "Logical CPU Cores", "8", "Possible Turbo Bins", "0", "Turbo Overclockable", "False",
        "Feature Flags", "EIST, TM2, PCID, FPU, VME, PSE, MSR, PAE, MCE, APIC, MTRR, PAT, PSE-36, ACPI, SS, HTT, TM", 
        "Instructions", "TSC, MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, AESNI, AVX", 
        "Intel® Turbo Boost Max", "False", "Intel® Speed Shift", "False", "Microcode Update", "0xD6", 
        "Hybrid Core Architecture", "No", 

        "Graphics",
        "Name", "NVIDIA GeForce GTX 960M", "Compatibility", "NVIDIA", "RAM", "2.00 GB", 
        "DAC Type", "Integrated RAMDAC", "Driver Version", "27.21.14.6109", "Driver Date", "31/12/2020", 
        "Name", "Intel(R) HD Graphics 530", "Compatibility", "Intel Corporation", "RAM", "1.00 GB", 
        "DAC Type", "Internal", "Driver Version", "20.19.15.4454", "Driver Date", "4/5/2016", 
        
        "Operating System", 
        "Manufacturer", "Microsoft Corporation", "Name", "Microsoft Windows 10 Home Single Language", 
        "Version", "10.0.19042", "Service Pack", "N/A", "System Name", "DESKTOP-ETBRV1U", 
        "Boot Device", "\\Device\\HarddiskVolume3", 
        
        "Watchdog", 
        "Watchdog Present", "Supported", "Running at Boot", "False", "Failed", "False", 
        
        "Memory", 
        "Total Installed Memory", "8.00 GB", "Bank Label", 
        "BANK 0", "Device Locator", "ChannelA-DIMM0", "Default Speed", "2133 MHz", "Capacity", "4.00 GB", 
        "Manufacturer", "SK Hynix", "Bank Label", 
        "BANK 2", "Device Locator", "ChannelB-DIMM0", "Default Speed", "2133 MHz", "Capacity", "4.00 GB", 
        "Manufacturer", "Kingston", 
        
        "BIOS", 
        "Manufacturer", "American Megatrends Inc.", "Version", "E16J5IMS.119", "Release Date", "15/2/2017", 
        
        "Motherboard", 
        "Manufacturer", "Micro-Star International Co., Ltd.", "Model", "MS-16J5", "Version", "REV:0.A", 
        "Serial Number", "BSS-0123456789", "Asset Tag", "Default string", 
        
        "XTU", 
        "Service Version", "7.3.0.33", "Client Version", "7.3.0.33", 
        "XTU Session Id", "a9ffc2c6-8b9a-4d65-bd4f-b403b94f5ab2"]


def split_key_value(list_):
    """
    Reference: https://www.tutorialspoint.com/python-program-to-split-the-even-and-odd-elements-into-two-different-lists
    Return two list where the element with index 0, 2, 4, ... => key and 1, 3, 5, ... => value

    Args:
        list_ (list): List where the element will be splitted into key and value list.

    Returns:
        key (list): List with element where the index of the element is 0 when modulo with 2
                    (Remainder = 0 when divide by 2).
        value (list): List with elements with index that are not divisible by two.

    Example:
        list_ = ["Brand String", "Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz",
                 "Family", "Skylake"]
        key = ["Brand String", "Family"]
        value = ["Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz", "Skylake"]
    """
    key = [] 
    value = [] 
    for index, element in enumerate(list_): 
        if (index % 2 == 0): 
            key.append(element) 
        else: 
            value.append(element) 
    return key, value

class TestCase_split_key_value(unittest.TestCase):
    def test_split_key_value(self):
        list_ = ["Brand String", "Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz",
                 "Family", "Skylake"]
        expected_key = ["Brand String", "Family"]
        expected_value = ["Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz", "Skylake"]

        key, value = split_key_value(list_)
        self.assertEqual(expected_key, key)
        self.assertEqual(expected_value, value)


def get_system_information_list(list_: list, start: str, end: str) -> list:
    """
    Extract system information from system info list extract from XTU System Info Pane,
    and convert them into a key,value pair in a list with tuple element (zip).

    Args:
        list_ (list): System information extracted to XUT UI.
        start (str): Start element to iteration.
        end (str): End element for the iteration.

    Returns:
        list_ (list): Updated version of the argument (list_), iterated element is removed.
        device_list (list): Device information in list with key, value pair. Determined by the
                            "start" and "end"
    """
    device = []
    for element in (list_[:]):  # [:] means return the shallow copy of the new list, https://docs.python.org/3/tutorial/introduction.html#strings
        if element == start:
            list_.remove(element)
        elif element  != end:
            device.append(element)
            list_.remove(element)
        elif element == end:
            break
    key, value = split_key_value(device)
    device_list = list(zip(key, value))
    return list_, device_list

class TestCase_get_system_information_list(unittest.TestCase):
    def test_get_system_information_list(self):
        global list_
        temp = list_

        expected_new_list = ["Graphics", "Name", "NVIDIA GeForce GTX 960M", "Compatibility", "NVIDIA", 
                            "RAM", "2.00 GB", "DAC Type", "Integrated RAMDAC", "Driver Version", "27.21.14.6109",  
                            "Driver Date", "31/12/2020", "Name", "Intel(R) HD Graphics 530", "Compatibility", 
                            "Intel Corporation", "RAM", "1.00 GB", "DAC Type", "Internal", "Driver Version",
                            "20.19.15.4454", "Driver Date", "4/5/2016", "Operating System", "Manufacturer",
                            "Microsoft Corporation", "Name", "Microsoft Windows 10 Home Single Language", 
                            "Version", "10.0.19042", "Service Pack", "N/A", "System Name", "DESKTOP-ETBRV1U", 
                            "Boot Device", "\\Device\\HarddiskVolume3", "Watchdog", "Watchdog Present", "Supported", 
                            "Running at Boot", "False", "Failed", "False", "Memory", "Total Installed Memory", "8.00 GB", 
                            "Bank Label", "BANK 0", "Device Locator", "ChannelA-DIMM0", "Default Speed", "2133 MHz", 
                            "Capacity", "4.00 GB", "Manufacturer", "SK Hynix", "Bank Label", "BANK 2", "Device Locator", 
                            "ChannelB-DIMM0", "Default Speed", "2133 MHz", "Capacity", "4.00 GB", "Manufacturer", 
                            "Kingston", "BIOS", "Manufacturer", "American Megatrends Inc.", "Version", "E16J5IMS.119", 
                            "Release Date", "15/2/2017", "Motherboard", "Manufacturer", "Micro-Star International Co., Ltd.", 
                            "Model", "MS-16J5", "Version", "REV:0.A", "Serial Number", "BSS-0123456789", "Asset Tag", 
                            "Default string", "XTU", "Service Version", "7.3.0.33", "Client Version", "7.3.0.33", 
                            "XTU Session Id", "a9ffc2c6-8b9a-4d65-bd4f-b403b94f5ab2"]
        expected_processor_info_list = [("Brand String", "Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz"), ("Family", "Skylake"), 
                                ("Physical CPU Cores", "4"), ("Logical CPU Cores", "8"), ("Possible Turbo Bins", "0"), 
                                ("Turbo Overclockable", "False"), ("Feature Flags", "EIST, TM2, PCID, FPU, VME, PSE, MSR, PAE, " +
                                "MCE, APIC, MTRR, PAT, PSE-36, ACPI, SS, HTT, TM"), 
                                ("Instructions", "TSC, MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, AESNI, AVX"), 
                                ("Intel® Turbo Boost Max", "False"), ("Intel® Speed Shift", "False"), 
                                ("Microcode Update", "0xD6"), ("Hybrid Core Architecture", "No")]
        updated_list, processor_info_list = get_system_information_list(temp, start="Processor", end="Graphics")
        self.assertEqual(expected_new_list, updated_list)
        self.assertEqual(expected_processor_info_list, processor_info_list)

        pretty_dict = json.dumps(dict(processor_info_list), sort_keys=False, ensure_ascii=False, indent=4)

        graphic_dict = {'GRAPHIC_0': {'Name': 'NVIDIA GeForce GTX 960M', 'Compatibility': 'NVIDIA', 'RAM': '2.00 GB', 'DAC Type': 
                        'Integrated RAMDAC', 'Driver Version': '27.21.14.6109', 'Driver Date': '31/12/2020'}, 'GRAPHIC_1': 
                        {'Name': 'Intel(R) HD Graphics 530', 'Compatibility': 'Intel Corporation', 'RAM': '1.00 GB', 'DAC Type':
                        'Internal', 'Driver Version': '20.19.15.4454', 'Driver Date': '4/5/2016'}}
        system_info = {}
        system_info["Processor"] = dict(processor_info_list)

        system_info["Graphics"] = graphic_dict
        print(json.dumps(system_info, sort_keys=False, ensure_ascii=False, indent=4))



os_list = ["Operating System", "Manufacturer",
            "Microsoft Corporation", "Name", "Microsoft Windows 10 Home Single Language", 
            "Version", "10.0.19042", "Service Pack", "N/A", "System Name", "DESKTOP-ETBRV1U", 
            "Boot Device", "\\Device\\HarddiskVolume3", "Watchdog", "Watchdog Present", "Supported", 
            "Running at Boot", "False", "Failed", "False", "Memory", "Total Installed Memory", "8.00 GB", 
            "Bank Label", "BANK 0", "Device Locator", "ChannelA-DIMM0", "Default Speed", "2133 MHz", 
            "Capacity", "4.00 GB", "Manufacturer", "SK Hynix", "Bank Label", "BANK 2", "Device Locator", 
            "ChannelB-DIMM0", "Default Speed", "2133 MHz", "Capacity", "4.00 GB", "Manufacturer", 
            "Kingston", "BIOS", "Manufacturer", "American Megatrends Inc.", "Version", "E16J5IMS.119", 
            "Release Date", "15/2/2017", "Motherboard", "Manufacturer", "Micro-Star International Co., Ltd.", 
            "Model", "MS-16J5", "Version", "REV:0.A", "Serial Number", "BSS-0123456789", "Asset Tag", 
            "Default string", "XTU", "Service Version", "7.3.0.33", "Client Version", "7.3.0.33", 
            "XTU Session Id", "a9ffc2c6-8b9a-4d65-bd4f-b403b94f5ab2"]

temp, dump = get_system_information_list(os_list, start="Operating System", end="Watchdog")
print(json.dumps(dict(dump), sort_keys=False, ensure_ascii=False, indent=4))

temp, dump = get_system_information_list(os_list, start="Watchdog", end="Memory")
print(json.dumps(dict(dump), sort_keys=False, ensure_ascii=False, indent=4))

# Memory got more than one device so have to split to another function just like graphics...
temp, dump = get_system_information_list(os_list, start="Memory", end="BIOS")
print(json.dumps(dict(dump), sort_keys=False, ensure_ascii=False, indent=4))

temp, dump = get_system_information_list(os_list, start="BIOS", end="XTU")
print(json.dumps(dict(dump), sort_keys=False, ensure_ascii=False, indent=4))

# Okay... Last one is abit tricky...
temp, dump = get_system_information_list(os_list, start="XTU", end="XTU Session Id")
print(json.dumps(dict(dump), sort_keys=False, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    unittest.main()