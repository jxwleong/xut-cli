import re

# Example of Monitor log from XTU
# MonitorLog2021-03-27_19-42-02-296.txt
# Regex: MonitorLog(\d{4}-\d{2}-\d{2})_(\d{2}-\d{2}-\d{2}-\d{3})

pattern = 'MonitorLog(\\d{4}-\\d{2}-\\d{2})_(\\d{2}-\\d{2}-\\d{2}-\\d{3})'
a = re.findall(pattern,  'MonitorLog2021-03-27_19-42-02-296.txt')
print(len(a))
a_list = list(a[0])
print(a_list)
# Replace '-' => ''
print(type(a_list[0]))
a_list[0] = a_list[0].replace('-', '')
a_list[1] = a_list[1].replace('-', '')
print(a_list)
time = ''.join(a_list)
print(time)