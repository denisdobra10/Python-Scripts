# Auto install dependencies ######################################
import os
import sys
import subprocess
import random
import time

try:
    import pyautogui
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
    import pyautogui


os.system('cls' if os.name == 'nt' else 'clear')

##################################################################

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! READ THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# INFO:
# IF THERE IS ANY ERROR ON DEPENDENCIES INSTALLATION
# JUST RUN pip install BY YOURSELF

# EXAMPLE (type this in console and press enter):
# pip install pyautogui

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! READ THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# List of goodbye messages
goodbye_messages = ['Goodbye!', "I'm outta here!", 'See you later!', 'Till next time!', 'Ciao!', 'Gotta go!']

while True:
    command = input('Enter a command (ss or exit/x): ')
    if command == 'ss':
        # Countdown from 5 to 1
        for i in range(5, 0, -1):
            print(i)
            time.sleep(1)
        # Take a screenshot
        screenshot = pyautogui.screenshot()
        # Generate a random 7-letter filename
        filename = ( ''.join(random.choices([chr(i) for i in range(ord('a'), ord('z')+1)], k=7)) )+ ".jpeg"
        # Save the screenshot to a file with the generated filename
        screenshot.save(filename)
        print(f"Screenshot successfully taken! It was saved on the disk under the following name: {filename}")
    elif command in ['exit', 'x']:
        # Exit the loop and print a random goodbye message
        print(random.choice(goodbye_messages))
        break
    else:
        print('Invalid command!')
