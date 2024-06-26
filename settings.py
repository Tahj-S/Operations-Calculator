import os
import sys
import time

creditsoff = 0
usercall = 0

while True:
    print ("What would you like to change:")
    set = input ("1. Turn On/Off Credits (on by default on startup) \n 2. Allow saying your username on run 0. Save changes \n")
    if set == "1":
        while True:
            crset = input ("Turn on or off credits? (yes/no) ")
            if crset == "off":
                creditsoff = 0
                print ("sucsessfully turned off credits")
                break

            elif crset == "on":
                creditsoff = 1
                print ("sucsessfully turned on credits")
                break
        
            else:
                print ("Invalid Option")
    elif set == "2":
        while True:
            usrset = input("Allow username calling on run? (yes/no) ")
            if usrset == "yes":
                usercall = 1
                print("Enter a username you want the system to say")
                username = input ("[?] ")
                f.open('config/user/username.txt', 'r')
                f.write(username)
                f.close()
            elif usrset == "no":
                usercall = 0
    elif set == "0":
        print("saving...")
        f.open('config/settings/creditsoff.txt', 'r')
        f.write(creditsoff)
        f.close()
        time.sleep(2)
        f.open('config/settings/usersay.txt', 'w')
        f.write(usercall)
        f.close() 
        os.startfile(main.py)
