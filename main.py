#Read first names into an array
from operator import concat
import random


firstNameFile = open("firstnames.txt", "r")
listOfFirstNames = []

while True:
    name = firstNameFile.readline()

    if not name:
        break
    else:
        listOfFirstNames.append(name.strip())

firstNameFile.close()

#Read last names into an array
lastNameFile = open("lastnames.txt", "r")
listOfLastNames = []

while True:
    name = lastNameFile.readline()

    if not name:
        break
    else:
        listOfLastNames.append(name.strip())

lastNameFile.close()

#Read knicknames into an array
knicknameFile = open("listOfNicknames.txt", "r")
listOfKnicknames = []

while True:
    name = knicknameFile.readline()

    if not name:
        break
    else:
        listOfKnicknames.append(name.strip())

knicknameFile.close()

firstName = listOfFirstNames[random.randint(0, len(listOfFirstNames)-1)]
lastName = listOfLastNames[random.randint(0, len(listOfLastNames)-1)]
knickname = listOfKnicknames[random.randint(0, len(listOfKnicknames)-1)]

print(firstName + " " + lastName + " aka "+knickname)
