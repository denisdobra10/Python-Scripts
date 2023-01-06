import difflib
import os
import json


# Database functionality
dbFilePath = os.getcwd() + "//db.txt"
database = {}


def updateDb():
    with open(dbFilePath, 'w') as f:
        json.dump(database, f)


def loadDb():
    with open(dbFilePath, 'r') as f:
        global database
        database = json.load(f)


def countDbObjects():
    loadDb()
    return len(database)

# End of database functionality



def ask(question):
    if question in database:
        return database[question]
    else:
        # Check if question as string is similar to something found in database
        closest_match = difflib.get_close_matches(question, database.keys(), n=1, cutoff=0.6)
        if closest_match:
            answer = database[closest_match[0]]
            print(f"I'm not sure about that, but I think the answer is '{answer}'. Is this correct?")
            
            # Check if bot was right by asking the user
            correct = input().lower()
            if correct in ["yes", "y"]:
                return answer
            else:
                print("I am sorry for that... Please provide the correct answer so I can learn and improve my AI brain.")
                correct_answer = input()
                database[question] = correct_answer
                updateDb()
                return correct_answer
        else:
            to_continue = input("I don't know the answer to that question. Do you wish to [continue] adding more information to your current question, [provide] the correct answer or [abort] this question?: ").lower()
            
            if to_continue in "continue":
                question_extrainfo = input()
                ask(question + ' ' + question_extrainfo)
            elif to_continue in 'provide':
                # Make the bot learn if there is no similar question found in database
                print("What is the correct answer?")
                correct_answer = input()
                database[question] = correct_answer
                updateDb()
                return correct_answer
            else:
                return 'Skipping the answer for this question'
                


# Main function for the program
def main():
    # Loading database
    loadDb()

    # Looping while user's input is not the willing to close the program
    while True:
        question = input("Ask me something: ")

        # Condition to exit the program
        if question.lower() in ["quit", "exit"]:
            break

        answer = ask(question)
        if answer != None:
            print("...-> ", answer)


# Actually starting the program
main()
# Goodbye message when user closes the program
print("Have a wonderful day!")