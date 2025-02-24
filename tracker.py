import json
from pythonFiles.setup import setup
from pythonFiles.getHistory import getHistory
from pythonFiles.addTransaction import addTransaction
from pythonFiles.getBalance import getBalance
from pythonFiles.getLanguage import getLanguage

lang = getLanguage()

action = setup()

if action == 1:

    getHistory()

if action == 2:

    addTransaction()

    print("")

    if lang == 2 or lang == "2":

        print("Transaction ajoutées avec succès")

    if lang == 1 or lang == "1":

        print("The transaction was successfully added")
        
    print("")
    
    exit(1)