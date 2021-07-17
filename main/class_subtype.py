import re

def class_st_check():
    class_list = "[a-cA-C]"
    print("What Class Subnet are you dealing with? \nCurrently only Class A, B and C are supported.")
    class_type = input("Class: ")
    if(re.search(class_list, class_type)):
        class_a()
    else:
        print("nope, try again")
        class_st_check()

def class_a():
    print("You have chosen Class A! \nWhat data would you like to search with, to find your remaining subnet information? \nChoose between: Network Bits(NB), Subnet Mask(SM), Bits Borrowed(BB), Subnets(SN), or Number of Hosts(NH).")
    cl_a = "^NB$|^nb$|^SM$|^sm$|^BB$|^bb$|^SN$|^sn$|^NH$|^nh$"
    user_in = input()
    if(re.search(cl_a, user_in)):
        print("You selected: {}".format(user_in))
        
    else:
        print("Try again!")
        class_a()

