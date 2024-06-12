import subprocess
import time
import sys

while True:
  y = int(input("Enter a number: "))
  x = int(input("Enter a second number: "))

  while True:
    time.sleep(2)
    operation = input("Choose your operation: ")

    if operation == "add":

      print ("Calculating...")

      time.sleep(2)

      print ("almost there...")

      time.sleep(2)

      print(y, "Plus", x, "Equals:", y + x)
      break

    elif operation == "subtract":

      print ("Calculating...")

      time.sleep(2)

      print ("almost there...")

      time.sleep(2)

      print(y, "subtracted by", x, "Equals:", y - x)
      break


    elif operation == "multiply":
      print ("Calculating...")

      time.sleep(2)

      print ("almost there...")

      time.sleep(2)

      print(y, "Multiplied by", x, "Equals:", y * x)
      break

    elif operation == "divide":
      print ("Calculating...")

      time.sleep(2)

      print ("almost there...")

      time.sleep(2)

      print (y, "divided by", x, "Equals:", y / x)
      break

    elif operation == "help":

      print ("add, subtract, multiply, divide, switch, and quit")

    elif operation == "quit":
      subprocess.run(["python", "main.py"])
      sys.exit()

    elif operation == "switch":
      break

    else:
      print ("Invalid operation")