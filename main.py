import random
import string


def wrongInput():
    print("Wrong input! Please try again.")
    return


def generateRandomCharacters(stringLength=0, options=0):
    # TODO - Check if the result have characters that user wanted
    choosenString = {
        0: string.ascii_lowercase,
        1: string.ascii_letters,
        2: string.ascii_lowercase + string.punctuation,
        3: string.ascii_letters + string.punctuation,
    }
    result = ""
    print(stringLength)  # + " \n " + type(stringLength))
    for i in range(stringLength):
        result += random.choice(choosenString[options])
    return result


# Main
repeat = 1
while (repeat == 1):

    # First Question
    length = int(input("How long the password should be? "))

    # Second Question
    option = 0
    while True:
        uppercase = input(
            "Do you want to generate password with uppercase letters? (Y)es / (N)o : ").lower().strip()
        if (uppercase == "y"):
            option += 1
            break
        elif (uppercase == "n"):
            break
        else:
            wrongInput()

    # Third Question
    while(True):
        specialCharacters = input(
            "Do you want to generate password with special characters? (Y)es / (N)o : ").lower().strip()
        if (specialCharacters == "y"):
            option += 2
            break
        elif (specialCharacters == "n"):
            break
        else:
            wrongInput()

    print(generateRandomCharacters(length, option))

    while True:
        uppercase = input(
            "Do you want to do it one more time? (Y)es / (N)o : ").lower().strip()
        if (uppercase == "y"):
            break
        elif (uppercase == "n"):
            repeat = 0
            break
        else:
            wrongInput()
