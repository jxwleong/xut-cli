import re
import os
# Example of Monitor log from XTU
# MonitorLog2021-03-27_19-42-02-296.txt
# Regex: MonitorLog(\d{4}-\d{2}-\d{2})_(\d{2}-\d{2}-\d{2}-\d{3})

def tuple2list(tuple_):
    """
    Convert matched pattern tuple to list.
    Expect single tuple in a list
    
    :param tuple_ (tuple): Matched pattern tuple
    :return (list): list with same element as tuple_

    :Example:
    [('2021-03-27', '13-35-36-346')] => ['2021-03-27', '13-35-36-346']
    """
    return list(tuple_[0])

pattern = 'MonitorLog(\\d{4}-\\d{2}-\\d{2})_(\\d{2}-\\d{2}-\\d{2}-\\d{3})'

a = re.findall(pattern,  'MonitorLog2021-03-27_19-42-02-296.txt')

def get_log_timestamp(log, pattern):
    """
    Get timestamp of MonitorLog name using regular expression

    :param log (str): Name of MonitorLog
    :param pattern (str): Regular expression pattern
    :return (tuple): Matched pattern tuple

    :Example:
    MonitorLog2021-03-27_19-42-02-296.txt => [('2021-03-27', '19-42-02-296')] 
    """
    return re.findall(pattern,  log)

def remove_dash_in_list(list_):
    """
    Remove the dash for str element in list,
    Expect list with two str elements.

    :param list_ (list): List with str element (MonitorLog)
    :return (list): List with dash removed from it's str element

    :Example:
    ['2021-03-27', '19-34-24-832'] => ['20210327', '193424832']
    """
    new_list = []
    if len(list_) == 2:
       for element in list_:
            new_element = element.replace('-', '')
            new_list.append(new_element)
    return new_list


def log_timestamp_to_integer(log):
    """
    Convert the timestamp in str from the name of MonitorLog
    to integer

    :param log (str): Name of the log file
    :return (int): The timestamp of the log file in integer (concatenated)

    :Example:
    MonitorLog2021-03-27_19-34-24-832.txt => 20210327193424832
    """

# # Replace '-' => ''
# print(type(a_list[0]))
# a_list[0] = a_list[0].replace('-', '')
# a_list[1] = a_list[1].replace('-', '')
# print(a_list)
# time = ''.join(a_list )
# print(time)

# latestlog = '0'

# loglist = os.listdir(r'C:\ProgramData\Intel\Intel Extreme Tuning Utility\Monitor Logs')
# for log in loglist:
#     print(log)
#     a = re.findall(pattern,  log)
#     print(a)
#     a_list = list(a[0])
#     a_list[0] = a_list[0].replace('-', '')
#     a_list[1] = a_list[1].replace('-', '')
#     print(a_list)
#     time = ''.join(a_list )
#     time = int(time)
#     print(time)
#     print(type(time))

#     try:
#         if "MonitorLog" in latestlog:
#             a = re.findall(pattern,  log)
#             print(a)
#             a_list = list(a[0])
#             a_list[0] = a_list[0].replace('-', '')
#             a_list[1] = a_list[1].replace('-', '')
#             print(a_list)
#             time = ''.join(a_list )
#             latestlog = int(time)
#     except: 
#         pass

#     if int(time) > int(latestlog):
#         latestlog = log

# print(f"Latest log: C:\ProgramData\Intel\Intel Extreme Tuning Utility\Monitor Logs\{log}")