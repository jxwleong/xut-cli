
import re

list = ["Memory", "Total Installed Memory", "8.00 GB", 
        "Bank Label", "BANK 0", "Device Locator", "ChannelA-DIMM0",
        "Default speed", "2133 MHz", "Capacity", "4.00 GB",
        "Manufacturer", "SK Hynix",
        "Bank Label", "Bank 2", "Device Locator", "ChannelB-DIMM0",
        "Default speed", "2133 MHz", "Capacity", "4.00 GB",
        "Manufacturer", "Kingston"]

reg = re.compile("l.+st")
string = "least"
match = bool(re.match(reg, string))
print(match)

for n in list:
    if n in ["Bank Label"]: 
        print("")
    print(n)