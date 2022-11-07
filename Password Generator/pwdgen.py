# PASSWORD GENERATOR BY DENIS @ 2022
import random
import pyperclip

# Setting up constants
letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k' ,'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
specialChars = [ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '`', '~', '[', ']', '{', '}', ';', ',', '.', '<', '>', '/', '?' ]
capitalLetters = []
for l in letters:
    capitalLetters.append(l.upper())


def GeneratePassword():
    # Preparing variables for generator
    desiredCharacters = "".join(letters)
    passLength = -1
    password = ""

    # Getting user's desired password length from input
    while(passLength == -1):
        try:
            passLength = int(input("How long would you like your password to be?(enter a number): "))
        except ValueError:
            print("You should enter a number! Try again")
    

    # Asking user if he would like capital letters into the generated password
    userInput = ""
    while(userInput.lower() != 'yes' and userInput.lower() != 'no'):
        userInput = input("Would you like to have capital letters into your password?(type yes or no): ")
    
    if(userInput.lower() == 'yes'):
        desiredCharacters += "".join(capitalLetters)

    # Asking user if he would like numbers into the generated password
    userInput = ""
    while(userInput.lower() != 'yes' and userInput.lower() != 'no'):
        userInput = input("Would you like to have numbers into your password?(type yes or no): ")
    
    if(userInput.lower() == 'yes'):
        desiredCharacters += "".join(numbers)

    # Askkng user if he would like special characters into the generated password
    userInput = ""
    while(userInput.lower() != 'yes' and userInput.lower() != 'no'):
        userInput = input("Would you like to have special characters into your password?(type yes or no): ")
    
    if(userInput.lower() == 'yes'):
        desiredCharacters += "".join(specialChars)


    # Generate the password based on user's preferences
    while(len(password) < passLength):
        randomIndex = random.randint(0, len(desiredCharacters))
        password += desiredCharacters[randomIndex]

    return password


generatedPassword = GeneratePassword()
print("Password has been successfully generated based on your preferences!: PASSWORD: {}".format(generatedPassword))

# Copy password to clipboard if user wants to
userInput = ""
while(userInput.lower() != "yes" and userInput.lower() != "no"):
    userInput = input("Would you like to copy the generated password to clipboard?(yes or no): ")
        

if(userInput.lower() == "yes"):
    pyperclip.copy(generatedPassword)
    print("Your generated password has been successfully copied to clipboard!")


print("Thanks for using PWDGen by Denis @ 2022")