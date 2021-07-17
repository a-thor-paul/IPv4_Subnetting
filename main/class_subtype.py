import re

def class_st_check():
    class_list = "[a-cA-C]"
    print("\nWhat Class Subnet are you dealing with? \nCurrently only Class A, B and C are supported.")
    class_type = input("\nClass: ")
    if(re.search(class_list, class_type)):
        class_a()
    else:
        print("nope, try again")
        class_st_check()

def class_a():
    print("\nYou have chosen Class A! \n\nWhat data would you like to search with, to find your remaining subnet information?Choose one of the following options: \n - Network Bits (NB)\n - Subnet Mask (SM)\n - Bits Borrowed (BB)\n - Subnets (SN)\n - Number of Hosts (NH)")
    cl_a = "^NB$|^nb$|^SM$|^sm$|^BB$|^bb$|^SN$|^sn$|^NH$|^nh$"
    user_in = input()
    if(re.search(cl_a, user_in)):
        print("You selected: {}".format(user_in))
        
    else:
        print("Try again!")
        class_a()

