import os
import subprocess
import time

creditsoff = 1
descriptions = 0

os.system("clear")
ascii_art_math = [
    "     ___                      _   _                  ",
    r"    /___\_ __   ___ _ __ __ _| |_(_) ___  _ __  ___  ",
    r"   //  // '_ \ / _ \ '__/ _` | __| |/ _ \| '_ \/ __| ",
    r"  / \_//| |_) |  __/ | | (_| | |_| | (_) | | | \__ \ ",
    r"  \___/ | .__/ \___|_|  \__,_|\__|_|\___/|_| |_|___/ ",
    "        |_|                                          "
]
for line in ascii_art_math:
  print(line)

time.sleep(1)
print("\n")
print("Simple Math Calculator in The Python Console \n")
print("---------------------------------------")
print("\n Made By: \n Tahj-S \n")
print("---------------------------------------")
time.sleep(2)

while True:
  os.system("clear")
  print("\n Welcome to the Operations Calculator")
  menu = input(
      "\n What would you like to do: \n 1. Make A calculation. \n 2. Print Pi. \n 3. Settings \n 4. Quit \n"
  )
  if menu == "1":
    subprocess.run(["python", "calculate.py"])

  elif menu == "2":
    subprocess.run(["python", "pi.py"])

  elif menu == "3":
    os.system("clear")
    while True:
      print ("What would you like to change:")
      set = input ("\n 1. Turn On/Off Credits (Off by defaultp) \n 2. Turn On/Off Descriptions (Off by deafault) \n")
      if set == "1":
        crset = input ("Turn on or off credits? ")
        if crset == "off":
          creditsoff = 1
          print ("sucsessfully turned off credits")
          break

        elif crset == "on":
          creditsoff = 0
          print ("sucsessfully turned on credits")
          break
        
        else:
          print ("Invalid Option")
          
      elif set == "2":
        descset = input ("Turn on or off descriptions? ")
        if descset == "off":
          descriptions = 0
          print ("sucsessfully turned off descriptions")
          break

        elif descset == "on":
          descriptions = 1
          print ("sucsessfully turned on descriptions")
          break
        
        else:
          print ("Invalid Option")
      else:
        print ("Invalid Option")
  elif menu == "4":
    credits = input("Are you sure you want to quit (y/n): ")
    if credits == "y":
      print("\n ---------------------------------------")
      time.sleep(1)
      break
      
    elif credits == "n":
      print("\n ---------------------------------------")

    else:
      print("\n Invalid Input, Taking you back to the menu")
      print("\n ---------------------------------------")

  elif menu == "5":
    print("You are now being taken to the beta version")
    print ("\n ---------------------------------------")
    time.sleep(1)
    subprocess.run(["python", "test/test.py"])
  
  else:
    print("Invalid Option")



if creditsoff == 0:
  os.system("clear")
  
  ascii_art_math2 = [

  "     ___                      _   _                  ",
  r"    /___\_ __   ___ _ __ __ _| |_(_) ___  _ __  ___  ",
  r"   //  // '_ \ / _ \ '__/ _` | __| |/ _ \| '_ \/ __| ",
  r"  / \_//| |_) |  __/ | | (_| | |_| | (_) | | | \__ \ ",
  r"  \___/ | .__/ \___|_|  \__,_|\__|_|\___/|_| |_|___/ ",
  "        |_|                                          "

  ]
  for lineabout in ascii_art_math2:
      print(lineabout)
  
  time.sleep(2)
  print ("\n")
  print ("A Simple Calculator Written in python \n")
  time.sleep(1)
  print ("---------------------------------------")
  time.sleep(2)
  print ("\n Made By: \n Tahj-S \n")
  time.sleep(1)
  print ("---------------------------------------")
  time.sleep(2)
  if descriptions == 1:
    print ("\n Special Thanks: \n VivaanMC - the thinks Javascript is better coder \n Mr.Unkown - A Fan of single board computers \n The Robotics Team - Idk if I can say much due to public Releases \n")
  else:
    print ("\n Special Thanks: \n VivaanMC \n Mr.Unkown \n The Robotics Team \n")
  time.sleep(1)
  print ("---------------------------------------")
  time.sleep(2)
  print ("\n And You!")
  time.sleep(2)
  print("\n Thank you for using Operations Calculator! \n")
  time.sleep(5)
  
  exit()

elif creditsoff == 1:
  exit()