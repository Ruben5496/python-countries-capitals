#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import OrderedDict
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import sys
import time
import smtplib
import getpass
COUNTRI = []
CAP = []
COUNTRI_AND_CAP = {}
def email():
    print "Send email by gmail"
    fromaddr = raw_input("Count from gmail: ")
    password = getpass.getpass("Password: ")
    toaddrs = raw_input("to: ")
   #asunto = raw_input("subject, from message: ")
    body = "Countries===========Capitals\n"
    for msg in COUNTRI_AND_CAP:
        body = body +str(msg).center(20)+str(COUNTRI_AND_CAP[msg]).center(30) + "\n"
        msg = MIMEMultipart()
        msg['From'] = fromaddr #This saves the mail of the sender
        msg['To'] = toaddrs  #This saves the mail of the receiver
        msg['Subject'] = "Countries and Capitals"  #This saves the subject
        msg.attach(MIMEText(body, 'plain')) #This saves the message
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddrs, text)
        server.quit()
        print "yes"
        raw_input("press enter")
    except smtplib.SMTPAuthenticationError:
        raw_input("No se envio nada\n Press enter to continue")

def Clear():
    os.system("cls")
    os.system("clear")
def Ordered():
    Clear()
    print """========================================="""
    print """|-----Countries----|--------Capitals----|"""
    print """|__________________|____________________|"""
    print """|                  |                    |"""
    ordered = OrderedDict(sorted(COUNTRI_AND_CAP.items(), key=lambda x: x[1:]))
    for key, value in ordered.items():
        print key.center(20) + value.center(10)
    raw_input("Press Enter to Continue")
    Clear()
def CountriesCapitalLists():
    print ">>>Countries and Capital Lists:<<< \n"
    for key in COUNTRI_AND_CAP:
        print key.center(20), COUNTRI_AND_CAP[key] + "\n"
    raw_input("Press enter to Continue")
    MENU()
    Clear()
def OnlyCount():
    print "     >>>COUNTRIES<<< \n"
    for key in COUNTRI_AND_CAP:
        print key.center(10)
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
        Count = str(Count).capitalize()
        for char in Count:
            if  char.isdigit() == False:
                Coun = False
            else:
                print "i don't understand the instruction"
                Coun = True
                raw_input("Press Enter to Continue")
                break
    cap = True
    while cap == True:
        capi = raw_input(">>>Please insert a Capital<<<\n")
        capi = capi.capitalize()
        for char in capi:
            if  char.isdigit() == False:
                cap = False
            else:
                print "i don't understando the instruction"
                cap = True
                break
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
        elif DATA == "4" or DATA == "All":
            CountriesCapitalLists()
        elif DATA == "5" or DATA == "AllOrdered":
            Ordered()
        elif DATA == "6" or DATA == "AllMail":
            email()
        elif DATA == "7" or DATA == "exit":
            EXIT()
        else:
            print "***Fatal Error***\n I don't understand the Instruction"
            raw_input("Press enter to insert another option\n")
            os.system("cls")
            os.system("clear")
MENU()
