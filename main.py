import subprocess
import sys
import time

creditsoff = 0


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

print("\n")
print("Simple Math Calculator in The Python Console \n")
print("---------------------------------------")
print("\n Made By: \n Tahj-S \n")
print("---------------------------------------")
print("\n Welcome to the Operations Calculator")

while True:
  menu = input(
      "\n What would you like to do: \n 1. Make A calculation. \n 2. Print Pi. \n 3. Settings \n 4. Quit \n"
  )
  if menu == "1":
    subprocess.run(["python", "calculate.py"])

  elif menu == "2":
    subprocess.run(["python", "pi.py"])

  elif menu == "3":
    while True:
      print ("What would you like to change:")
      set = input ("1. Turn On/Off Credits (on by default on startup) \n")
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

  else:
    print("Invalid Option")



if creditsoff == 0:
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
  print ("\n Special Thanks: \n VivaanMC - the thinks Javascript is better coder \n Mr.Unkown - A Fan of single board computers \n")
  time.sleep(1)
  print ("---------------------------------------")
  time.sleep(2)
  print ("\n And You!")
  time.sleep(2)
  print("\n Thank you for using Operations Calculator! \n")
  time.sleep(5)
  
  sys.exit()

elif creditsoff == 1:
  sys.exit()