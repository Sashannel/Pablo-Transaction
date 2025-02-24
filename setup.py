import json
from pythonFiles.getBalance import getBalance
from pythonFiles.language import Language
from pythonFiles.getLanguage import getLanguage

def setup():

    for i in range(5):

        print("")

    print("--------------------")
    print("")
    print("PABLO EXPENSE TRACKER")

    for i in range(6):
        print("")

    Language()
    lang = getLanguage()

    if lang == 2 or lang == "2":

        print("Vous possédez actuellement", getBalance(), "€")

    if lang == 1 or lang == "1":

        print("You own", getBalance(), "$")

    print("")

    if lang == 2 or lang == "2":

        print("1: Voir l'historique des transactions")
        print("2: Ajouter une transaction")

    if lang == 1 or lang == "1":

        print("1: See transaction history")
        print("2: Add a new transaction")

    print("")

    read = input()

    if read == "1":

        return 1
    
    if read == "2":

        return 2
    
    else:

        if lang == 2 or lang == "2":

            print("Entrée invalide")

        if lang == 1 or lang == "1":

            print("Invalid input")