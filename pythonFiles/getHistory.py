import json
from pythonFiles.getLanguage import getLanguage

def getHistory():

    lang = getLanguage()

    print("")

    if lang == 2 or lang == "2":

        print("Voici l'historique de vos transactions:")

    if lang == 1 or lang == "1":

        print("Here's your transaction history:")

    print("")

    with open("./data/data.json", "r") as file:

        content = json.load(file)

    names = list(content.keys())
    values = list(content.values())

    for i in range(len(content)):

        if values[i] < 0:

            spaces = 20 - len(list(names[i]))
            space = []

            for j in range(spaces):

                space.append(" ")
            
            space = ''.join(space)

            if lang == 2 or lang == "2":

                print("DEPENSE", names[i], space, ":     ", values[i])

            if lang == 1 or lang == "1":

                print("EXPENSE", names[i], space, ":     ", values[i])

        if values[i] >= 0:

            spaces = 20 - len(list(names[i]))
            space = []

            for j in range(spaces):

                space.append(" ")
            
            space = ''.join(space)

            if lang == 2 or lang == "2":

                print("ENTREE ", names[i], space, ":     ", values[i])

            if lang == 1 or lang == "1":

                print("INCOME", names[i], space, ":     ", values[i])

    for i in range(3):

        print("")
