import subprocess
import sys
import time

creditsoff = 1


print("\n Hi", "Welcome to the Operations Calculator")

while True:
  menu = input(
      "\n What would you like to do: \n 1. Make A calculation. \n 2. Print Pi. \n 3. Settings \n 4. Quit \n"
  )
  if menu == "1":
    subprocess.run(["python", "calculate.py"])

  elif menu == "2":
    subprocess.run(["python", "pi.py"])

  elif menu == "3":
    subprocess.run(["python", "settings.py"])

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

if creditsoff == 1:
  sys.exit()