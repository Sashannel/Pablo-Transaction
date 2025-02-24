import json

def getBalance():
        
    content = {}

    with open("./data/data.json", "r") as file:
        content = json.load(file)

    return sum(content.values())