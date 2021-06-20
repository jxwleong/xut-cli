import unittest
import copy
import json

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


def get_system_information_list(list_: list, start: str, end: str=None) -> list:
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
        else:   # If end is None
            continue
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


def get_size_of_element(list_, start, end):
    """
    Get the size of the element so that we know when to stop if
    there's more than one devices.
    The purpose of this is because the key of dictionary must be unique
    If there're more than one devices, the dictionary will only register the later
    elements.
    The workaround is the split devices into separate dictionary

    Args:
        list_ (list): Value from list(zip(list1, list2)). EX:
                      graphic_list = [('Name', 'NVIDIA GeForce GTX 960M'), ('Compatibility', 'NVIDIA'), ('RAM', '2.00 GB'), 
                                    ('DAC Type', 'Integrated RAMDAC'), ('Driver Version', '27.21.14.6109'), ('Driver Date', '31/12/2020'), 
                                    ('Name', 'Intel(R) HD Graphics 530'), ('Compatibility', 'Intel Corporation'), ('RAM', '1.00 GB'), 
                                    ('DAC Type', 'Internal'), ('Driver Version', '20.19.15.4454'), ('Driver Date', '4/5/2016')]
        start (str): Start key
        end (str): End key

    Example (start - Name, end - Name):
        Name: NVIDIA GeForce GTX 960M
        Compatibility: NVIDIA
        RAM: 2.00 GB
        DAC Type: Integrated RAMDAC
        Driver Version: 27.21.14.6109
        Driver Date: 31/12/2020
        Name: Intel(R) HD Graphics 530
    For this example, the size of the elements is 6.
    Which will be used to iterated over the list.

    Returns: 
        int: Size of the elements each devices
    """
    START_KEY_FOUND = False
    count = 0
    for element in list_:
        key, value = element
        if key == start and START_KEY_FOUND is False:
            START_KEY_FOUND = True
            count += 1
        elif key == end and START_KEY_FOUND is True:
            return count  # Multiply by 2 because it's dict
        else:
            count += 1
    raise Exception(f"\nlist_: {list_}\n"
                    f"start: {start}\n"
                    f"end: {end}\n"
                    f"Either the start or end is NOT in the list_.")

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


def remove_multiple_element_in_list(list_: list, element_to_remove: list) -> list:
    """ Remove the elements in a list and return the updated list.
 
    Args:
        list_ (list): List where the elements will be removed. 
        element_to_remove (list): List which specified the elements to be remove in list_.

    Returns:
        updated_list (list): List where the elements specified in element_to_remove are 
                             removed.
    """
    for element in element_to_remove:
        list_.remove(element)
    return list_

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


def list_with_dict_element_to_dict(list_: list, prefix: str):
    """
    Convert list element (must be dict) and create a nested dict.\n
    Number of element of list_ must be > 1

    Args:
        list_ (list): List where the dict elements will be used to create a nested dict
        prefix (str): Str to be prefix as key of the nested dict.

    Returns:
        dict_ (dict): Dict where the elements are extracted from list_
    """
    dict_ = {}
    if len(list_) <= 1: raise Exception(f"Expecting list with multiple element but received list with {len(list_)} element")
    for index, element in enumerate(list_):
        if isinstance(element, dict) is False:  raise TypeError(f"Expecting dict element in list_ but received {element}")
        dict_[prefix + str(index)] = element
    return dict_

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


def get_graphic_info(list_):
    """ Get graphics info after extract the text from XTU UI (TEMP)

    Args:
        list_ (list): List which the element contain list of tuples that consist
                      information about graphics. Example,
                        graphic_list = [('Name', 'NVIDIA GeForce GTX 960M'), ('Compatibility', 'NVIDIA'), ('RAM', '2.00 GB'), 
                            ('DAC Type', 'Integrated RAMDAC'), ('Driver Version', '27.21.14.6109'), ('Driver Date', '31/12/2020'), 
                            ('Name', 'Intel(R) HD Graphics 530'), ('Compatibility', 'Intel Corporation'), ('RAM', '1.00 GB'), 
                            ('DAC Type', 'Internal'), ('Driver Version', '20.19.15.4454'), ('Driver Date', '4/5/2016')]
    Returns:
        dict_ (dict): Nested dictionary that contain the memory information extract from system pane of XUT.
                      Example:
                        'Graphics': {'GRAPHIC_0': {'Name': 'NVIDIA GeForce GTX 960M', 
                        'Compatibility': 'NVIDIA', 'RAM': '2.00 GB', 'DAC Type': 'Integrated RAMDAC', 'Driver Version': '27.21.14.6109', 
                        'Driver Date': '31/12/2020'}, 'GRAPHIC_1': {'Name': 'Intel(R) HD Graphics 530', 'Compatibility': 'Intel Corporation', 
                        'RAM': '1.00 GB', 'DAC Type': 'Internal', 'Driver Version': '20.19.15.4454', 'Driver Date': '4/5/2016'}}
    """
    graphics = []
    graphic_dict = {}
    device_element_size = get_size_of_element(list_, "Name", "Name")
    number_of_device = int(len(list_)/device_element_size)

    for main_index in range(0, number_of_device):
        iterated_element = []
        for index in range(0, device_element_size):
            element = list_[index]
            key, value = element
            graphic_dict[key] = value
            iterated_element.append(element)
        list_ = remove_multiple_element_in_list(list_, iterated_element)
        # Shallow copy is required otherwise next iteration, it will replace the existing copy because
        # It's not deep copy since I'm not messing with nested element :)
        # The next iteration will replace the existing graphic_dict
        graphic_dict_shallow_copy = copy.copy(graphic_dict)
        graphics.append(graphic_dict_shallow_copy)      

    graphic_dict = list_with_dict_element_to_dict(list_=graphics, prefix="GRAPHIC_")
    return graphic_dict

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


def get_memory_info(list_):
    """ Get memory info after extract the text from XTU UI (TEMP)

    Args:
        list_ (list): List which the element contain list of tuples that consist
                      information about graphics. Example,
                        memory_list = [('Total Installed Memory', '8.00 GB'), ('Bank Label', 'BANK 0'), ('Device Locator', 'ChannelA-DIMM0'), 
                        ('Default Speed', '2133 MHz'), ('Capacity', '4.00 GB'), ('Manufacturer', 'SK Hynix'), ('Bank Label', 'BANK 2'), 
                        ('Device Locator', 'ChannelB-DIMM0'), ('Default Speed', '2133 MHz'), ('Capacity', '4.00 GB'), ('Manufacturer', 'Kingston')]
    Returns:
        dict_ (dict): Nested dictionary that contain the memory information extract from system pane of XUT.
                      Example:
                      'Memory': {'Total Installed Memory': '8.00 GB', 'Memory Module(s)': 
                        {'MEMORY_0': {'Bank Label': 'BANK 0', 'Device Locator': 'ChannelA-DIMM0', 'Default Speed': '2133 MHz', 
                        'Capacity': '4.00 GB', 'Manufacturer': 'SK Hynix'}, 'MEMORY_1': 
                        {'Bank Label': 'BANK 2', 'Device Locator': 'ChannelB-DIMM0', 'Default Speed': '2133 MHz', 
                        'Capacity': '4.00 GB', 'Manufacturer': 'Kingston'}}}
    """
    memory = []
    memory_module_dict = {}
    memory_dict = {}
    # Place the first element of the list [("Total Installed Memory", "8.00 GB"), (..., ...)]
    # As first element of the main memory_dict
    memory_dict[list_[0][0]] = list_[0][1]
    list_.remove(list_[0])
    device_element_size = get_size_of_element(list_, "Bank Label", "Bank Label")
    number_of_device = int(len(list_)/device_element_size)

    for main_index in range(0, number_of_device):
        iterated_element = []
        for index in range(0, device_element_size):
            element = list_[index]
            key, value = element
            memory_module_dict[key] = value
            iterated_element.append(element)
        list_ = remove_multiple_element_in_list(list_, iterated_element)
        # Shallow copy is required otherwise next iteration, it will replace the existing copy because
        # It's not deep copy since I'm not messing with nested element :)
        # The next iteration will replace the existing graphic_dict
        memory_module_dict_shallow_copy = copy.copy(memory_module_dict)
        memory.append(memory_module_dict_shallow_copy)      

    memory_module_dict = list_with_dict_element_to_dict(list_=memory, prefix="MEMORY_")
    memory_dict["Memory Module(s)"] = memory_module_dict # Combine the dict
    return memory_dict

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

def get_all_system_info(list_):
    """Extract all the devices information.

    Args:
        list_ (list): List that contain the all system information extract from using uiautomation module.
                      Example on the top of this module.

    Returns:
        system_info (dict): All the information extract from XUT System Info Pane in dictionary format.
    """
    system_info = {}

    _, processor_list = get_system_information_list(list_, start="Processor", end="Graphics")
    system_info["Processor"] = dict(processor_list)
    _, graphic_list = get_system_information_list(list_, start="Graphics", end="Operating System")
    system_info["Graphics"] = get_graphic_info(graphic_list)
    _, operating_system = get_system_information_list(list_, start="Operating System", end="Watchdog")
    system_info["Operating System"] = dict(operating_system)
    _, watchdog = get_system_information_list(list_, start="Watchdog", end="Memory")
    system_info["Watchdog"] = dict(watchdog)
    _, memory_list = get_system_information_list(list_, start="Memory", end="BIOS")
    memory = get_memory_info(memory_list)
    system_info["Memory"] = dict(memory)
    _, bios = get_system_information_list(list_, start="BIOS", end="Motherboard")
    system_info["BIOS"] = dict(bios)
    _, motherboard = get_system_information_list(list_, start="Motherboard", end="XTU")
    system_info["Motherboard"] = dict(motherboard)
    _, xtu = get_system_information_list(list_, start="XTU")
    system_info["XTU"] = dict(xtu)

    return system_info

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