#THIS FILE IS FOR TESTING PURPOSES ONLY; TREAD CAREFULLY
import re
from Units import UnitsFlat
from Locale import getStr
import csv

txts=["Ich gehe 12 mi 12312",
"Du bewegst dich 1249in",
"Das Ziel ist 3 meter entfernt",
"Ich gehe 3dfs",
"Er ist 2 Jahre alt",
"Ich sehe 3d"]

#print( getStr("GER", "CONVERSION_EMBED_TITLE") )


with open("Zauber.tsv", "r", encoding='UTF-8', newline='') as file:
    raw = csv.DictReader(file, delimiter="\t", quotechar="'", quoting=csv.QUOTE_NONE)
    for spell in raw:
        spell["Beschreibung"]=spell["Beschreibung"].replace("\\n", "\n")
        print(spell)

