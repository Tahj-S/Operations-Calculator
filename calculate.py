import subprocess
import time
import sys

while True:
  y = int(input("Enter a number: "))
  x = int(input("Enter a second number: "))

  while True:
    time.sleep(2)
    operation = input("Choose your operation: ")

    if operation == "add" or "+":

      print(y, "Plus", x, "Equals:", y + x)
      break

    elif operation == "subtract" or "-":

      print(y, "subtracted by", x, "Equals:", y - x)
      break

    elif operation == "multiply" or "*":

      print(y, "Multiplied by", x, "Equals:", y * x)
      break

    elif operation == "divide" or "/":

      print (y, "divided by", x, "Equals:", y / x)
      break

    elif operation == "help" or "?":

      print ("""
      add (+)
      subtract (-)
      multiply (*)
      divide (/)
      help(?)
      switch (.)
      quit (!)
      """)

    elif operation == "quit":
      subprocess.run(["python", "main.py"])
      sys.exit()

    elif operation == "switch":
      break

    else:
      print ("Invalid operation")

    else:
      print ("Invalid operation")
