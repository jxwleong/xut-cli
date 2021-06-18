import pprint
import json

list_  = ['Processor', 'Brand String', 'Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz', 'Family', 'Skylake', 'Physical CPU Cores', '4', 'Logical CPU Cores', '8', 
        'Possible Turbo Bins', '0', 'Turbo Overclockable', 'False', 'Feature Flags', 'EIST, TM2, PCID, FPU, VME, PSE, MSR, PAE, MCE, APIC, MTRR, PAT, PSE-36, ACPI, SS, HTT, TM', 
        'Instructions', 'TSC, MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, AESNI, AVX', 'Intel® Turbo Boost Max', 'False', 'Intel® Speed Shift', 'False', 'Microcode Update', '0xD6', 
        'Hybrid Core Architecture', 'No', 'Graphics', 'Name', 'NVIDIA GeForce GTX 960M', 'Compatibility', 'NVIDIA', 'RAM', '2.00 GB', 'DAC Type', 'Integrated RAMDAC', 
        'Driver Version', '27.21.14.6109', 'Driver Date', '31/12/2020', 'Name', 'Intel(R) HD Graphics 530', 'Compatibility', 'Intel Corporation', 'RAM', '1.00 GB', 'DAC Type', 
        'Internal', 'Driver Version', '20.19.15.4454', 'Driver Date', '4/5/2016', 'Operating System', 'Manufacturer', 'Microsoft Corporation', 'Name', 'Microsoft Windows 10 Home Single Language', 
        'Version', '10.0.19042', 'Service Pack', 'N/A', 'System Name', 'DESKTOP-ETBRV1U', 'Boot Device', '\\Device\\HarddiskVolume3', 'Watchdog', 'Watchdog Present', 'Supported', 
        'Running at Boot', 'False', 'Failed', 'False', 'Memory', 'Total Installed Memory', '8.00 GB', 'Bank Label', 'BANK 0', 'Device Locator', 'ChannelA-DIMM0', 'Default Speed', 
        '2133 MHz', 'Capacity', '4.00 GB', 'Manufacturer', 'SK Hynix', 'Bank Label', 'BANK 2', 'Device Locator', 'ChannelB-DIMM0', 'Default Speed', '2133 MHz', 'Capacity', '4.00 GB', 
        'Manufacturer', 'Kingston', 'BIOS', 'Manufacturer', 'American Megatrends Inc.', 'Version', 'E16J5IMS.119', 'Release Date', '15/2/2017', 'Motherboard', 'Manufacturer', 
        'Micro-Star International Co., Ltd.', 'Model', 'MS-16J5', 'Version', 'REV:0.A', 'Serial Number', 'BSS-0123456789', 'Asset Tag', 'Default string', 'XTU', 'Service Version', '7.3.0.33', 
        'Client Version', '7.3.0.33', 'XTU Session Id', 'a9ffc2c6-8b9a-4d65-bd4f-b403b94f5ab2']

def split_key_value(list_):
    """
    Reference: https://www.tutorialspoint.com/python-program-to-split-the-even-and-odd-elements-into-two-different-lists
    Return two list where the 0, 2, 4, ... => key and 1, 3, 5, ... => value
    """
    key = [] 
    value = [] 
    for index, element in enumerate(list_): 
        if (index % 2 == 0): 
            key.append(element) 
        else: 
            value.append(element) 
    return key, value

processor = []
for index, element in enumerate(list_[:]):  # [:] means return the shallow copy of the new list, https://docs.python.org/3/tutorial/introduction.html#strings
    if element == "Processor":
        list_.remove(element)
    elif element != "Graphics":
        #print(f"{element}")
        processor.append(element)
        list_.remove(element)
    elif element == "Graphics":
        break
#print(list_)

#print(processor)
key, value = split_key_value(processor)
processor_info = dict(zip(key,value))

print("PROCESSOR")
print(processor_info)
# ensure_ascii is needed in order to print the copyright sign
# else will just print \u00ae
print(json.dumps(processor_info, sort_keys=False, ensure_ascii=False, indent=4))