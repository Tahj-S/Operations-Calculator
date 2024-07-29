import math
import subprocess
import time
import sys

print("Almost There...")

time.sleep(2)

print ("PI(π)", "is equal to:", math.pi)
menu = input ("Would you like to go back to the main menu?(y/n)")
if menu == "y":
  subprocess.run(["python", "main.py"])
  sys.exit()
elif menu == "n":
  print ("\n Thank you for using the Operations Calculator.")
  print ("\n Since we are still working on more feature for pi actions.")
  print("\n we are sending you back to the main menu any way.")
  time.sleep(3)
  subprocess.run(["python", "main.py"])
  sys.exit()
else:
  print ("Invalid Option")
  subprocess.run(["python", "main.py"])
  sys.exit()