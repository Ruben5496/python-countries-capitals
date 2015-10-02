import os
import sys
COUNTRI = []
CAP = []
COUNTRI_AND_CAP = {
    "COUNTRI"
    "CAP"
}
def COUNTRIES():
    raw_input(">>>Please insert a Country and his Capital<<<\n")
def EXIT():
    print "I hope you like it.\n See you again n.n"
    raw_input(">>>Press Enter for Continue<<<")
    sys.exit()
def MENU():
    os.system("cls")
    print "Welcome\n"
    print "#1 Countries"
    print "#2 Capitals"
    print "#3 Countries and Capital Lists"
    print "#4 Countries and Capitals ordered by Capital"
    print "#5 All by mail"
    print "#6 Exit"
    DATA = raw_input(">>>Select an Option<<<\n")
    if DATA == "1":
        COUNTRIES()
    elif DATA == "2":
        CAPITALS()
    elif DATA == "3":
        COUNTRIES_AND_CAPITALS()
    elif DATA == "4":
        ORDERED()
    elif DATA == "5":
        MAIL()
    elif DATA == "6":
        EXIT()
    else:
        print "***Fatal Error***\n I don't understand the Instruction"
        raw_input("Press enter to insert another option\n")
        os.system("cls")
MENU()