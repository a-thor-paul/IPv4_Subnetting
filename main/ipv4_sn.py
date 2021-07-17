#This program will allow the user to input IPv4 data such as:
#Network Bits, Subnet Mask, Bits Borrowed, total Subnets, 
#and total Hosts to get the full Subnet Information.
#The use of this program is for when only partial subnet information
#has been provided to the user.

import re
import class_subtype

class_subtype.class_st_check()
#Regex for IP format xxx.xxx.xxx
#ip_add = "[0-9]\d{1,3}\.[0-9]\d{1,3}\.[0-9]\d{1,3}"

#if (re.search(ip_add, class_type)):
#    print(class_type)
#else:
#    print("nope")