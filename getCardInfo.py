import urllib.request
import urllib.parse
import json


def sortByKey(val):
    return val["title"]

# Get the foil price in USD
def getCardJson(cardName):
    cardUrl = "https://api.scryfall.com/cards/named?exact="+ urllib.parse.quote('"' + cardName + '"')
    with urllib.request.urlopen(cardUrl) as url:
        data = url.read()
        encoding = url.info().get_content_charset('utf-8')

    cardData = json.loads(data.decode(encoding))

    return cardData 

def prettyPrintJson(jsonObj):
    print(json.dumps(jsonObj, indent=4, sort_keys=True))

# example code to show you how to access the json info
if __name__ == "__main__":
    # get the card json and print it
    damnation = getCardJson('damnation')
    prettyPrintJson(damnation)


    print("***************************************")
    print("name: " + damnation["name"])
    print("***************************************")
    print("mana cost: " + damnation["mana_cost"])
    print("***************************************")
    print("oracle text:")
    print(damnation["oracle_text"])
