import copy
import os
import sys
import unittest
import json

REPO_ROOT = os.path.abspath(os.path.join(__file__, "..", ".."))
sys.path.insert(0, REPO_ROOT)

from system_info import *


# System info list extract from ui automation...
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



class TestCase_split_key_value(unittest.TestCase):
    def test_split_key_value(self):
        list_ = ["Brand String", "Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz",
                 "Family", "Skylake"]
        expected_key = ["Brand String", "Family"]
        expected_value = ["Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz", "Skylake"]

        key, value = split_key_value(list_)
        self.assertEqual(expected_key, key)
        self.assertEqual(expected_value, value)




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



class TestCase_get_size_of_element(unittest.TestCase):
    def test_get_size_of_element(self):
        graphic_list = [('Name', 'NVIDIA GeForce GTX 960M'), ('Compatibility', 'NVIDIA'), ('RAM', '2.00 GB'), 
                    ('DAC Type', 'Integrated RAMDAC'), ('Driver Version', '27.21.14.6109'), ('Driver Date', '31/12/2020'), 
                    ('Name', 'Intel(R) HD Graphics 530'), ('Compatibility', 'Intel Corporation'), ('RAM', '1.00 GB'), 
                    ('DAC Type', 'Internal'), ('Driver Version', '20.19.15.4454'), ('Driver Date', '4/5/2016')]
        self.assertEqual(6, get_size_of_element(graphic_list, "Name", "Name"))

    def test_get_size_of_element_throw_exception(self):
        graphic_list = [('Name', 'NVIDIA GeForce GTX 960M'), ('Compatibility', 'NVIDIA'), ('RAM', '2.00 GB'), 
                    ('DAC Type', 'Integrated RAMDAC'), ('Driver Version', '27.21.14.6109'), ('Driver Date', '31/12/2020'), 
                    ('Name', 'Intel(R) HD Graphics 530'), ('Compatibility', 'Intel Corporation'), ('RAM', '1.00 GB'), 
                    ('DAC Type', 'Internal'), ('Driver Version', '20.19.15.4454'), ('Driver Date', '4/5/2016')]
        self.assertRaises(Exception, get_size_of_element, graphic_list, "Name", "aaa")




class TestCase_remove_multiple_element_in_list(unittest.TestCase):
    def test_remove_multiple_element_in_list(self):
        list_ = [1, 2, 3]
        element_to_be_remove = [1, 2]
        updated_list = remove_multiple_element_in_list(list_, element_to_be_remove)
        
        self.assertEqual([3], updated_list)

    def test_remove_multiple_element_in_list_given_element_not_in_list(self):
        list_ = [1, 2, 3]
        element_to_be_remove = [1, "G"]
        
        self.assertRaises(ValueError, remove_multiple_element_in_list, list_, element_to_be_remove)




class TestCase_list_with_dict_element_to_dict(unittest.TestCase):
    def test_list_with_dict_element_to_dict(self):
        list_ = [{'Name': 'NVIDIA GeForce GTX 960M', 'Compatibility': 'NVIDIA', 'RAM': '2.00 GB', 'DAC Type': 'Integrated RAMDAC', 
                'Driver Version': '27.21.14.6109', 'Driver Date': '31/12/2020'}, 
                {'Name': 'Intel(R) HD Graphics 530', 'Compatibility': 'Intel Corporation', 'RAM': '1.00 GB', 'DAC Type': 'Internal', 
                'Driver Version': '20.19.15.4454', 'Driver Date': '4/5/2016'}]
        expected_dict = {'GRAPHIC_0': {'Name': 'NVIDIA GeForce GTX 960M', 'Compatibility': 'NVIDIA', 'RAM': '2.00 GB', 'DAC Type': 
                        'Integrated RAMDAC', 'Driver Version': '27.21.14.6109', 'Driver Date': '31/12/2020'}, 'GRAPHIC_1': 
                        {'Name': 'Intel(R) HD Graphics 530', 'Compatibility': 'Intel Corporation', 'RAM': '1.00 GB', 'DAC Type':
                        'Internal', 'Driver Version': '20.19.15.4454', 'Driver Date': '4/5/2016'}}
        self.assertEqual(expected_dict, list_with_dict_element_to_dict(list_, prefix="GRAPHIC_"))
        
    def test_list_with_dict_element_to_dict_given_one_element_expect_Exception(self):
        list_ = [{"Name": "Intel"}]
        self.assertRaises(Exception, list_with_dict_element_to_dict, list_, prefix="GRAPHIC_")

    def test_list_with_dict_element_to_dict_given_non_dict_elements_expect_TypeError(self):
        list_ = [["G", "A"], [1, 3]]
        self.assertRaises(TypeError, list_with_dict_element_to_dict, list_, prefix="GRAPHIC_")

        list_ = [["G", "A"], {"Key": 3}]
        self.assertRaises(TypeError, list_with_dict_element_to_dict, list_, prefix="GRAPHIC_")



class TestCase_get_graphic_info(unittest.TestCase):
    def test_get_graphic_info(self):
        graphic_list = [('Name', 'NVIDIA GeForce GTX 960M'), ('Compatibility', 'NVIDIA'), ('RAM', '2.00 GB'), 
                ('DAC Type', 'Integrated RAMDAC'), ('Driver Version', '27.21.14.6109'), ('Driver Date', '31/12/2020'), 
                ('Name', 'Intel(R) HD Graphics 530'), ('Compatibility', 'Intel Corporation'), ('RAM', '1.00 GB'), 
                ('DAC Type', 'Internal'), ('Driver Version', '20.19.15.4454'), ('Driver Date', '4/5/2016')]

        graphic_dict = get_graphic_info(graphic_list)
        expected_graphic_dict = {'GRAPHIC_0': {'Name': 'NVIDIA GeForce GTX 960M', 'Compatibility': 'NVIDIA', 'RAM': '2.00 GB', 
                                'DAC Type': 'Integrated RAMDAC', 'Driver Version': '27.21.14.6109', 'Driver Date': '31/12/2020'}, 
                                'GRAPHIC_1': {'Name': 'Intel(R) HD Graphics 530', 'Compatibility': 'Intel Corporation', 'RAM': '1.00 GB', 
                                'DAC Type': 'Internal', 'Driver Version': '20.19.15.4454', 'Driver Date': '4/5/2016'}}
        self.assertEqual(expected_graphic_dict, graphic_dict)



class TestCase_get_memory_info(unittest.TestCase):
    def test_get_memory_info(self):
        memory_list = [('Total Installed Memory', '8.00 GB'), ('Bank Label', 'BANK 0'), ('Device Locator', 'ChannelA-DIMM0'), 
                    ('Default Speed', '2133 MHz'), ('Capacity', '4.00 GB'), ('Manufacturer', 'SK Hynix'), ('Bank Label', 'BANK 2'), 
                    ('Device Locator', 'ChannelB-DIMM0'), ('Default Speed', '2133 MHz'), ('Capacity', '4.00 GB'), ('Manufacturer', 'Kingston')]
        memory_dict = get_memory_info(memory_list)
        expected_memory_dict = {'Total Installed Memory': '8.00 GB', 'Memory Module(s)': {'MEMORY_0': 
                                {'Bank Label': 'BANK 0', 'Device Locator': 'ChannelA-DIMM0', 'Default Speed': '2133 MHz', 'Capacity': '4.00 GB', 
                                'Manufacturer': 'SK Hynix'}, 
                                'MEMORY_1': {'Bank Label': 'BANK 2', 'Device Locator': 'ChannelB-DIMM0', 'Default Speed': '2133 MHz', 'Capacity': '4.00 GB', 
                                'Manufacturer': 'Kingston'}}}
        self.assertEqual(expected_memory_dict, memory_dict)



class TestCase_get_all_system_information(unittest.TestCase):
    def test_get_all_system_information(self):
        copied_list = copy.copy(list_)
        expected_system_info = {'Processor': {'Brand String': 'Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz', 
                    'Family': 'Skylake', 'Physical CPU Cores': '4', 'Logical CPU Cores': '8', 
                    'Possible Turbo Bins': '0', 'Turbo Overclockable': 'False', 
                    'Feature Flags': ('EIST, TM2, PCID, FPU, VME, PSE, MSR, PAE, MCE, APIC, MTRR, PAT, ' +
                    'PSE-36, ACPI, SS, HTT, TM'), 
                    'Instructions': 'TSC, MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, AESNI, AVX', 
                    'Intel® Turbo Boost Max': 'False', 'Intel® Speed Shift': 'False', 
                    'Microcode Update': '0xD6', 'Hybrid Core Architecture': 'No'}, 
                    'Graphics': {'GRAPHIC_0': {'Name': 'NVIDIA GeForce GTX 960M', 'Compatibility': 'NVIDIA', 
                    'RAM': '2.00 GB', 'DAC Type': 'Integrated RAMDAC', 
                    'Driver Version': '27.21.14.6109', 'Driver Date': '31/12/2020'}, 'GRAPHIC_1': 
                    {'Name': 'Intel(R) HD Graphics 530', 'Compatibility': 'Intel Corporation', 
                    'RAM': '1.00 GB', 'DAC Type': 'Internal', 'Driver Version': '20.19.15.4454', 
                    'Driver Date': '4/5/2016'}}, 
                    'Operating System': {'Manufacturer': 'Microsoft Corporation', 'Name': 'Microsoft Windows 10 Home Single Language', 
                    'Version': '10.0.19042', 'Service Pack': 'N/A', 'System Name': 'DESKTOP-ETBRV1U', 
                    'Boot Device': '\\Device\\HarddiskVolume3'}, 
                    'Watchdog': {'Watchdog Present': 'Supported', 'Running at Boot': 'False', 'Failed': 'False'}, 
                    'Memory': {'Total Installed Memory': '8.00 GB',
                    'Memory Module(s)': {'MEMORY_0': {'Bank Label': 'BANK 0', 'Device Locator': 
                    'ChannelA-DIMM0', 'Default Speed': '2133 MHz', 
                    'Capacity': '4.00 GB', 'Manufacturer': 'SK Hynix'}, 'MEMORY_1': {'Bank Label': 'BANK 2', 
                    'Device Locator': 'ChannelB-DIMM0', 
                    'Default Speed': '2133 MHz', 'Capacity': '4.00 GB', 'Manufacturer': 'Kingston'}}}, 
                    'BIOS': {'Manufacturer': 'American Megatrends Inc.', 
                    'Version': 'E16J5IMS.119', 'Release Date': '15/2/2017'}, 
                    'Motherboard': {'Manufacturer': 'Micro-Star International Co., Ltd.', 'Model': 'MS-16J5', 
                    'Version': 'REV:0.A', 'Serial Number': 'BSS-0123456789', 'Asset Tag': 'Default string'}, 
                    'XTU': {'Service Version': '7.3.0.33', 'Client Version': '7.3.0.33', 
                    'XTU Session Id': 'a9ffc2c6-8b9a-4d65-bd4f-b403b94f5ab2'}}
        system_info = get_all_system_info(copied_list)
        self.assertEqual(expected_system_info, system_info)

class TestCaseGetAllSystemInformation(unittest.TestCase):
    """
    Test Case to test the flow of extracting system information such as processor, graphics,
    memory and etc from the full system info list.
    The system info list is get from ui automation module.
    """
    def test_get_system_information(self):
        global list_
        copied_list = copy.deepcopy(list_)

        """
        Interestingly the elements of copied_list get removed within the function call...
        Just tested it, list.remove() inside a function will change the list element outside
        of the scope of the function.
        But during iteration need to use for element in list_[:], to remove other elements else
        it will only remove the first element.
        Seems to be have something to do with shallow copy...

        The result need further processing to combine all the lists of tuples to a nested dictionary.
        """
        expected_processor_list = [('Brand String', 'Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz'), 
                                    ('Family', 'Skylake'), ('Physical CPU Cores', '4'), ('Logical CPU Cores', '8'), 
                                    ('Possible Turbo Bins', '0'), ('Turbo Overclockable', 'False'), 
                                    ('Feature Flags', 'EIST, TM2, PCID, FPU, VME, PSE, MSR, PAE, MCE, APIC, MTRR, PAT, PSE-36, ACPI, SS, HTT, TM'), 
                                    ('Instructions', 'TSC, MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, AESNI, AVX'), 
                                    ('Intel® Turbo Boost Max', 'False'), ('Intel® Speed Shift', 'False'), 
                                    ('Microcode Update', '0xD6'), ('Hybrid Core Architecture', 'No')]
        _, processor_list = get_system_information_list(copied_list, start="Processor", end="Graphics")
        self.assertEqual(expected_processor_list, processor_list)

        expected_graphic_list = [('Name', 'NVIDIA GeForce GTX 960M'), ('Compatibility', 'NVIDIA'), ('RAM', '2.00 GB'), 
                                ('DAC Type', 'Integrated RAMDAC'), ('Driver Version', '27.21.14.6109'), ('Driver Date', '31/12/2020'), 
                                ('Name', 'Intel(R) HD Graphics 530'), ('Compatibility', 'Intel Corporation'), ('RAM', '1.00 GB'), 
                                ('DAC Type', 'Internal'), ('Driver Version', '20.19.15.4454'), ('Driver Date', '4/5/2016')]
        _, graphic_list = get_system_information_list(copied_list, start="Graphics", end="Operating System")
        self.assertEqual(expected_graphic_list, graphic_list)

        expected_operating_system_list = [('Manufacturer', 'Microsoft Corporation'), ('Name', 'Microsoft Windows 10 Home Single Language'), 
                                        ('Version', '10.0.19042'), ('Service Pack', 'N/A'), ('System Name', 'DESKTOP-ETBRV1U'), 
                                        ('Boot Device', '\\Device\\HarddiskVolume3')]
        _, operating_system_list = get_system_information_list(copied_list, start="Operating System", end="Watchdog")
        self.assertEqual(expected_operating_system_list, operating_system_list)

        expected_watchdog_list = [('Watchdog Present', 'Supported'), ('Running at Boot', 'False'), ('Failed', 'False')]
        _,  watchdog_list= get_system_information_list(copied_list, start="Watchdog", end="Memory")
        self.assertEqual(expected_watchdog_list, watchdog_list)

        expected_memory_list = [('Total Installed Memory', '8.00 GB'), ('Bank Label', 'BANK 0'), ('Device Locator', 'ChannelA-DIMM0'), 
                                ('Default Speed', '2133 MHz'), ('Capacity', '4.00 GB'), 
                                ('Manufacturer', 'SK Hynix'), ('Bank Label', 'BANK 2'), ('Device Locator', 'ChannelB-DIMM0'), 
                                ('Default Speed', '2133 MHz'), ('Capacity', '4.00 GB'), ('Manufacturer', 'Kingston')]
        _, memory_list = get_system_information_list(copied_list, start="Memory", end="BIOS")
        self.assertEqual(expected_memory_list, memory_list)

        expected_bios_list = [('Manufacturer', 'American Megatrends Inc.'), ('Version', 'E16J5IMS.119'), ('Release Date', '15/2/2017')]
        _, bios_list = get_system_information_list(copied_list, start="BIOS", end="Motherboard")
        self.assertEqual(expected_bios_list, bios_list)

        expected_motherboard_list = [('Manufacturer', 'Micro-Star International Co., Ltd.'), ('Model', 'MS-16J5'), 
                                    ('Version', 'REV:0.A'), ('Serial Number', 'BSS-0123456789'), ('Asset Tag', 'Default string')]
        _, motherboard_list = get_system_information_list(copied_list, start="Motherboard", end="XTU")
        self.assertEqual(expected_motherboard_list, motherboard_list)

        expected_xtu_list = [('Service Version', '7.3.0.33'), ('Client Version', '7.3.0.33'), ('XTU Session Id', 'a9ffc2c6-8b9a-4d65-bd4f-b403b94f5ab2')]
        _, xtu_list = get_system_information_list(copied_list, start="XTU")
        self.assertEqual(expected_xtu_list, xtu_list)

        # Expect iterate through all the elements in the list, and for each iteration
        # the element is removed. So expecting the final list would be empty.
        self.assertEqual([], copied_list)

if __name__ == "__main__":
    unittest.main()