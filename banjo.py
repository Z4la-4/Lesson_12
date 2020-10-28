

name = input("What is your name?\n")

def plays_banjo(name):
    if name[0].lower() == "r":
        return str(name.capitalize() + " plays banjo!")
    else:
        return str(name.capitalize() + " does not play banjo!")

print(plays_banjo(name))

