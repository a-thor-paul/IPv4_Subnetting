import mysql.connector
import mysql_connect
import re

def class_subtype_check():
    
    class_subtype_dict = {
        "A" : class_a,
        "B" : class_a,
        "C" : class_a,
    }

    #regex list to confirm option A, B or C is selected in lower/uppercase
    class_list = "^A$|^B$|^C$"
   
    print("\nWhat Class Subnet are you dealing with? \nCurrently only Class A, B and C are supported.")
    
    user_in = input("\nClass: ").upper()
    
    #regex search to confirm user input is in regex list
    if(re.search(class_list, user_in)):
        
        print("\nYou have chosen Class {}! \n\nWhat data would you like to search with, to find your remaining subnet information?\nChoose one of the following options: \n - Network Bits (NB)\n - Subnet Mask (SM)\n - Bits Borrowed (BB)\n - Subnets (SN)\n - Number of Hosts (NH)".format(user_in))

        class_subtype_dict[user_in]()

    else:
        print("nope, try again")
        class_subtype_check()

def net_bit():
    #print("It worked: Network bits")
    mysql_connect.ipv4_a()


def sub_mask():

    #print("It worked: Subnet Mask")
    
    #Regex for Subnet Mask format xxx.xxx.xxx.xxx
    ip_add = "[0-9]\d{0,3}\.[0-9]\d{0,3}\.[0-9]\d{0,3}\.[0-9]\d{0,3}"

    user_in = input("Type your subnet mask: ")

    if(re.search(ip_add, user_in)):
        print(user_in)

    else:
        print("gottem")

def bit_brw():
    print("It worked: Bits Borrowed")

def sub_nets():
    print("It worked: Subnets")

def num_host():
    print("It worked Number of Hosts")

class_dict = {
    "NB" : net_bit,
    "SM" : sub_mask,
    "BB" : bit_brw,
    "SN" : sub_nets,
    "NH" : num_host,
}

def class_a():
    
    #regex list to check if input matches options in lower or upper case
    cl_a = "^NB$|^SM$|^BB$|^SN$|^NH$"
    
    user_in = input("\nSelect an option: ").upper()

    #regex search to confirm user input is in regex list
    if(re.search(cl_a, user_in)):

        class_dict[user_in]()

    else:
        print("Try again!")
        class_a()

