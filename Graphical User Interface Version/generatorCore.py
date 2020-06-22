import random
import string

debugmode = False

def debug(str):
  if debugmode:
    for i in str:
      print(i)

setsOfCharacters = {
  3: string.ascii_lowercase,
  2: string.digits,
  1: string.punctuation,
  0: string.ascii_uppercase,
}

def printWarning(infoString=""):
  print("[Warning] "+infoString)

def generateRandomString(str, len):
  return "".join(random.SystemRandom().choice(str) for _ in range(len))

# Function for generating string with random character

def generateRandomCharacters(stringLength=0, options=0):

  def generateFormula(stringLength, sets=[]):
    numberOfSets = len(sets)
    setsTogether = "".join(sets)
    eachSetsCharacter = []
    if stringLength < numberOfSets:
      printWarning(
        "Length of the password is to short to include all types of the characters.")
      return generateRandomString(setsTogether, stringLength)
    else:
      stringLength -= len(sets)
      tempStringLength = stringLength
      for i in range(0, numberOfSets):
        debug([i,random.randint(0, len(sets[i])), sets[i][0], tempStringLength])
        randomCharacter = random.SystemRandom().choice(sets[i])
        eachSetsCharacter.append([randomCharacter, random.randint(0,tempStringLength)])
        tempStringLength += 1
      debug([eachSetsCharacter])
      result = generateRandomString(setsTogether,stringLength)
      for i in eachSetsCharacter:
        result = result[:i[1]] + i[0] + result[i[1]:]
      debug([setsTogether, result])
      return result

  chosenStrings = []
  tempOptions = options
  for i in range(3, 0-1, -1):
    if tempOptions >= 2 ** i:
      tempOptions = tempOptions-2**i
      chosenStrings.append(setsOfCharacters[i])

  if len(chosenStrings) == 0:
    print("You did not choose any set of characters.")

  return generateFormula(stringLength, chosenStrings)
