import os
import sys
import time

creditsoff = 0

while True:
    print ("What would you like to change:")
    set = input ("1. Turn On/Off Credits (on by default on startup) \n 0. Save changes")
    if set == "1":
        while True:
            crset = input ("Turn on or off credits? ")
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

    if set == "0":
        print("saving...")
        time.sleep(2)
        os.startfile(main.py)
