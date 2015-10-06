from collections import OrderedDict
import os
import sys
import time
import socket
import smtplib
COUNTRI = []
CAP = []
COUNTRI_AND_CAP = {}
def Clear():
    os.system("cls")
    os.system("clear")
"""def Mail(subject, text):
    print "Do you want to send this in a E-MAIL?"
    email = "@".join([os.getenv("LOGNAME"), socket.gethostname()])
    msg = ("From: {0}\nTo: {0}\nSubject: {1}\n{2}".format(email, subject, text))
    server = smtplib.SMTP("localhost")
    server.sendmail(email, email, msg)
    Clear()
    return
def main():
    """Main section"""

    send_mail_local("Comprobando el envío de correo localmente",
                    "Si puedes leer esto, tu servidor local SMTP está OK")

    print("Comprueba el correo en tu buzón local {0}\nEste normalmente se "
          "encuentra situado en /var/mail/{1}".
          format("@".join([os.getenv("LOGNAME"), socket.gethostname()]),
                 os.getenv("LOGNAME")))

    if __name__ == "__main__":
    main()"""
def Ordered():
    print """====================================="""
    print """|Countries                  Capitals|"""
    ordered = OrderedDict(sorted(COUNTRI_AND_CAP.items(), key=lambda x: x[1:]))
    for key, value in ordered.items():
        print key + "             " + value
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
        os.system("clear")
        COUNTRY()
        CAPITALS()
    elif quest == "n" or quest == "no":
        MENU()
    else:
        print "Insert a valid option"
        Questions()
def COUNTRY():
    os.system("cls")
    os.system("clear")
    Coun = True
    while Coun == True:
        Count = raw_input(">>>Please insert a Country<<<\n")
        Count = str(Count).title()
        if  Count.isalpha() == True or " " in Count:
            Coun = False
        else:
            print "i don't understand the instruction"
            Coun = True
            raw_input("Press Enter to Continue")
    cap= True       
    while cap == True:        
        capi = raw_input(">>>Please insert a Capital<<<\n")
        capi = capi.title()
        if  str(capi).isalpha() == True or " " in capi:
            cap = False
        else:
            print "i don't understando the instruction"
            cap = True   
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
        os.system("clear")
        print """========================================"""
        print """|-------COUNTRIES AND CAPITALS---------|"""
        print """========================================"""
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
            Mail()
        elif DATA == "7" or DATA == "exit":
            EXIT()
        else:
            print "***Fatal Error***\n I don't understand the Instruction"
            raw_input("Press enter to insert another option\n")
            os.system("cls")
            os.system("clear")    
MENU()