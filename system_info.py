import copy
import json


excluded_sysinfo_text = ["Welcome to Intel Extreme Tuning Utility",
            ("Intel Extreme Tuning Utility is a state-of-the-art overclocking solution for Intel IA-based platforms. " +
            "It is a comprehensive set of tools to tune, test and monitor your system." +
            "Click on the link to learn more about  Overclocking  and  XTU"),
            "How do I overclock with it?", 
            "The platform does not support overclocking. For best Overclocking performance, please check Intel K- and X-series Processors."]
sysinfo_title = ["Processor", "Graphics", "Operating System", "Watchdog", "Memory", "BIOS", "Motherboard", "XTU"]


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


def get_size_of_element(list_, start, end, wildcard=False):
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
        wildcard (bool): Set to True to ignore the exception if end is not meet with start.

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
    if wildcard is True: 
        count -= 1  # Minus the increment from previous for loop
        return count
    raise Exception(f"\nlist_: {list_}\n"
                    f"start: {start}\n"
                    f"end: {end}\n"
                    f"Either the start or end is NOT in the list_.")
 

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
    #if len(list_) <= 1: raise Exception(f"Expecting list with multiple element but received list with {len(list_)} element")
    for index, element in enumerate(list_):
        if isinstance(element, dict) is False:  raise TypeError(f"Expecting dict element in list_ but received {element}")
        dict_[prefix + str(index)] = element
    return dict_


    
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
    device_element_size = get_size_of_element(list_, "Name", "Name", wildcard=True)
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
    device_element_size = get_size_of_element(list_, "Bank Label", "Bank Label", wildcard=True)
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


