import json

def Language():

    print("What language would you like to use ?")
    print("")

    print("1: English")
    print("2: French")

    print("")

    langNum = input()

    print("")

    toWrite = {"language": langNum}

    object = json.dumps(toWrite, indent = 4)

    with open("./data/lang.json", "w") as file:

        file.write(object)
