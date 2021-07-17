import re

def class_st_check():
    
    #regex list to confirm option A, B or C is selected in lower/uppercase
    class_list = "^A$|^B$|^C$"
   
    print("\nWhat Class Subnet are you dealing with? \nCurrently only Class A, B and C are supported.")
    
    class_type = input("\nClass: ").upper()
    
    #regex search to confirm user input is in regex list
    if(re.search(class_list, class_type)):
        class_a()
    else:
        print("nope, try again")
        class_st_check()




def net_bit():
    print("It worked: Network bits")

def sub_mask():
    print("It worked: Subnet Mask")

def bit_brw():
    print("It worked: Bits Borrowed")

def sub_nets():
    print("It worked: Subnets")

def num_host():
    print("It worked Number of Hosts")

class_dict = {
    "NB" : net_bit,
    "SM" :sub_mask,
    "BB" : bit_brw,
    "SN" : sub_nets,
    "NH" : num_host,
}

def class_a():
    
    print("\nYou have chosen Class A! \n\nWhat data would you like to search with, to find your remaining subnet information?\nChoose one of the following options: \n - Network Bits (NB)\n - Subnet Mask (SM)\n - Bits Borrowed (BB)\n - Subnets (SN)\n - Number of Hosts (NH)")
    
    #regex list to check if input matches options in lower or upper case
    cl_a = "^NB$|^nb$|^SM$|^sm$|^BB$|^bb$|^SN$|^sn$|^NH$|^nh$"
    
    user_in = input("\nSelect an option: ").upper()

    #regex search to confirm user input is in regex list
    if(re.search(cl_a, user_in)):
        #print("\nYou selected: {}".format(user_in))
        class_dict[user_in]()
        
    else:
        print("Try again!")
        class_a()

