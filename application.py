from collections import OrderedDict
import os
import sys
import time
COUNTRI = []
CAP = []
COUNTRI_AND_CAP = {}
def Clear():
    os.system("cls")
def Ordered():
    ordered = OrderedDict(sorted(COUNTRI_AND_CAP.items(), key=lambda x: x[1:]))
    for key, value in ordered.items():
        print key, value
    raw_input("Press Enter to Continue")    
    Clear()
def CountriesCapitalLists():
    print "       >>>Countries and Capital Lists:<<< \n"
    for key in COUNTRI_AND_CAP:
        print key +"     " + COUNTRI_AND_CAP[key] + "\n" 
    raw_input("Press enter to Continue")   
    MENU()
    Clear()
def OnlyCount():
    print "     >>>COUNTRIES<<< \n"
    for key in COUNTRI_AND_CAP:
        print key + "\n" 

    raw_input("Press enter to Continue")
    MENU()
    Clear()
def OnlyCaps():
    print "     >>>Capitals<<<\n"
    for i in COUNTRI_AND_CAP:
        print COUNTRI_AND_CAP[i] + "\n" 
    raw_input("Press Enter to Continue")
    MENU()
    Clear()
def Questions():
    quest = raw_input("Do you want to Insert another Country? Y/N\n")
    quest = quest.lower()
    if quest == "y" or quest == "yes":
        os.system("cls")
        COUNTRY()
        CAPITALS()
    elif quest == "n" or quest == "no":
        MENU()
    else:
        print "Insert a valid option"
        Questions()
def COUNTRY():
    os.system("cls")
    Count = raw_input(">>>Please insert a Country<<<\n")
    Count = Count.lower()
    capi = raw_input(">>>Please insert a Capital<<<\n")
    capi = capi.lower()
    COUNTRI_AND_CAP[Count] = capi
    Questions()
    MENU()
def EXIT():
    print "I hope you like it.\n See you again n.n"
    time.sleep(2)
    sys.exit()
def MENU():
    while True:
        os.system("cls")
        print "Welcome\n"
        print "#1 Insert a Country"
        print "#2 Countries"
        print "#3 Capitals"
        print "#4 Countries and Capital Lists"
        print "#5 Countries and Capitals ordered by Capital"
        print "#6 All by mail"
        print "#7 Exit"
        DATA = raw_input(">>>Select an Option<<<\n")
        DATA = DATA.lower()
        if DATA == "1" or DATA == "country":
            COUNTRY()
        elif DATA == "2" or DATA == "Countries":
            OnlyCount()
        elif DATA == "3" or DATA == "Capitals":
            OnlyCaps()
        elif DATA == "4":
            CountriesCapitalLists()
        elif DATA == "5":
            Ordered()
        elif DATA == "6":
            mail()
        elif DATA == "7" or DATA == "exit":
            EXIT()
        else:
            print "***Fatal Error***\n I don't understand the Instruction"
            raw_input("Press enter to insert another option\n")
            os.system("cls")    
MENU()