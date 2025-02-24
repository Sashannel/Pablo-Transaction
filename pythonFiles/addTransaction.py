import json
from pythonFiles.getLanguage import getLanguage

def addTransaction():

    lang = getLanguage()

    if lang == 2 or lang == "2":
        
        print("")
        print("Quel est le nom de la transaction ?")
        name = input()
        
        print("")
        print("Quel est le montant de la transaction ?")
        amount = input()
        
    
    if lang == 1 or lang == "1":

        print("")
        print("What is the transaction's name ?")
        name = input()

        print("")
        print("How much money is it worth ?")
        amount = input()

    if amount.isnumeric == False:

        if lang == 2 or lang == "2":

            print("Le montant doit être un nombre !")

        if lang == 1 or lang == "1":

            print("The amount of money has to be a number !")

        exit(1)

    toWrite = {name: int(amount)}

    content = {}

    with open("./data/data.json", "r") as file:

        content = json.load(file)

    toWrite.update(dict(content))

    object = json.dumps(toWrite, indent = 4)

    with open("./data/data.json", "w") as file:

        file.write(object)

    return name, amount
