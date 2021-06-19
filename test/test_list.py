import copy
import unittest
import json

graphic_list = [('Name', 'NVIDIA GeForce GTX 960M'), ('Compatibility', 'NVIDIA'), ('RAM', '2.00 GB'), 
        ('DAC Type', 'Integrated RAMDAC'), ('Driver Version', '27.21.14.6109'), ('Driver Date', '31/12/2020'), 
        ('Name', 'Intel(R) HD Graphics 530'), ('Compatibility', 'Intel Corporation'), ('RAM', '1.00 GB'), 
        ('DAC Type', 'Internal'), ('Driver Version', '20.19.15.4454'), ('Driver Date', '4/5/2016')]

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
        list_ (list): List that contain system information extract from the system pane UI of XUT.
                      Expecting the processor information is already removed from this list. So the
                      first element would be "Graphics" and it will iterate until it meet "Operating System"
    """
    graphics = []
    graphic_dict = {}
    device_element_size = get_size_of_element(graphic_list, "Name", "Name")
    number_of_device = int(len(list_)/device_element_size)

    for main_index in range(0, number_of_device):
        iterated_element = []
        for index in range(0, device_element_size):
            element = list_[index]
            key, value = element
            graphic_dict[key] = value
            iterated_element.append(element)
        list_ = remove_multiple_element_in_list(list_, iterated_element)
        # Deep copy is required otherwise next iteration, it will replace the existing copy because
        # if it's not deep copy then it just a reference to the original object instead if a full
        # clone.
        # The next iteration will replace the existing graphic_dict
        deep_copy_graphic_dict = copy.deepcopy(graphic_dict)
        graphics.append(deep_copy_graphic_dict)      

    dict_ = list_with_dict_element_to_dict(list_=graphics, prefix="GRAPHIC_")
    print(json.dumps(dict_, sort_keys=False, ensure_ascii=False, indent=4))
    return dict_

get_graphic_info(graphic_list)

temp = [{'Name': 'NVIDIA GeForce GTX 960M', 'Compatibility': 'NVIDIA', 'RAM': '2.00 GB', 'DAC Type': 'Integrated RAMDAC', 
        'Driver Version': '27.21.14.6109', 'Driver Date': '31/12/2020'}, 
        {'Name': 'Intel(R) HD Graphics 530', 'Compatibility': 'Intel Corporation', 'RAM': '1.00 GB', 'DAC Type': 'Internal', 
        'Driver Version': '20.19.15.4454', 'Driver Date': '4/5/2016'}]





#print(dict_temp)
#print(json.dumps(dict_temp, sort_keys=False, ensure_ascii=False, indent=4))
#list_with_dict_element_to_dict([[1, 2], [3, 4]], "TEMP")
#============Operating System================

list_ = ['Operating System', 'Manufacturer', 'Microsoft Corporation', 'Name', 'Microsoft Windows 10 Home Single Language', 'Version', '10.0.19042', 'Service Pack', 'N/A', 'System Name', 'DESKTOP-ETBRV1U', 'Boot Device', '\\Device\\HarddiskVolume3', 
'Watchdog']

if __name__ == '__main__':
    unittest.main()