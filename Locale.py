
def getStr(lang:str, name:str, *args):
    if lang=="GER":
        return Strings[name][0]
    elif lang == "ENG":
        return Strings[name][1]
    else:
        return name

Strings = {
    "CONVERSION_EMBED_TITLE": ("Einheitenumrechnung","Unit Conversion")
    


    #Units
    **dict.fromkeys(['a', 'c', 'd'], ("Meilen", "miles"))
}