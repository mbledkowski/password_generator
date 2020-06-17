import generatorCore as generateCore


# Function that ask Yes or No type question and return 1 on 0

def askQuestion(question=''):
  while True:
    answer = input(question + ' (Y)es / (N)o : ').lower().strip()
    if answer == 'y':
      return 1
    elif answer == 'n':
      return 0
    else:
      print("Wrong input! Please try again.")


# Main
while True:

  # First Question
  while True:
    try:
      length = int(input("How long the password should be? Number : "))
      if length > 0:
        break
      elif length == 0:
        print("Value equal to ZERO does not make sense! Please try again.")
      elif length < 0:
        print(
          "Values smaller than ZERO do not make sense! Please try again.")
    except ValueError:
      print("Wrong input! Please try again.")

  # Questions about sets of characters - Choosen sets are stored in form of 4 digits long binary number.

  # First digit (2^3 / 8) stands for lowercase letters
  # Last digit (2^0 / 1) stands for uppercase letters
  # Third digit (2^1 / 2) stands for !@#./ like characters
  # Second digit (2^2 / 4) stands for digits

  option = 8

  if (askQuestion("Do you want to include uppercase letters?") == 1):
    option += 1

  if (askQuestion("Do you want to include special characters?") == 1):
    option += 2

  if (askQuestion("Do you want to include digits?") == 1):
    option += 4

  # Prints output from
  print("-------------------")
  print("Generated password:")
  print(generateCore.generateRandomCharacters(length, option))
  print("-------------------")

  if (askQuestion("Do you want to do this one more time?") == 0):
    break
