import re

def class_st_check():
    class_list = "[a-cA-C]"
    print("What Class Subnet are you dealing with? \nCurrently only Class A, B and C are supported.")
    class_type = input("Class: ")
    if(re.search(class_list, class_type)):
        print("You have chosen Class: {}".format(class_type))
    else:
        print("nope, try again")
        class_st_check()
