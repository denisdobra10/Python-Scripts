import cv2
import os
import json


def load_database():
    # Load the database from the "db.txt" file
    with open("db.txt", "r") as f:
        database = json.load(f)
    return database

def save_database(database):
    # Save the database to the "db.txt" file
    with open("db.txt", "w") as f:
        json.dump(database, f)



def main():
    # Load the Haar cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Get the current working directory
    cwd = os.getcwd()

    # Check if the "images" directory exists
    if not os.path.exists(os.path.join(cwd, "images")):
        # Create the "images" directory
        os.makedirs(os.path.join(cwd, "images"))

    # Get the list of files in the "images" directory
    files = os.listdir(os.path.join(cwd, "images"))

    # Check if the "images" directory is empty
    if len(files) == 0:
        print("You must have your photo selection inside the folder 'images'!")
    else:
        # Loading the database
        database = load_database()

        # Iterate over the files in the "images" directory
        for file in files:
            # Load the image and convert it to grayscale
            image_path = os.path.join(cwd, "images", file)
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = face_cascade.detectMultiScale(gray, 1.1, 5)

            # Check if any face was detected
            if len(faces) > 1:
                print("Multiple faces detected in this photo: {}".format(file))
            elif len(faces) == 1:
                # Check if image is found in database
                if image_path in database:
                    print("{} was found in the following file: {}!".format(database[image_path], file))
                    continue

                # If image is not found in database ask the user either to provide a name or to skip the process
                print("{} contains a human.".format(file))
                userchoice = input("I don't know who is this person... You can provide the name by typing it and pressing enter or you can write 'skip' to skip the process: ")

                if not 'skip' in userchoice.lower():
                    # Save the name of the person on this specific image
                    database[image_path] = userchoice
                    save_database(database)
            else:
                print("{} does not contain a human.".format(file))

    

# Start of the program
main()
