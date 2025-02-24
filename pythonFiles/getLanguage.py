import json

def getLanguage():

    with open("./data/lang.json", "r") as file:

        content = json.load(file)


    lang = list(content.values())[0]
    
    return str(lang)
